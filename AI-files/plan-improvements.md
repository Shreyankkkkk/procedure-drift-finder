# Implementation Plan: Procedure Drift Finder Professionalization

This plan evolves the Procedure Drift Finder from a hackathon prototype to a business-ready enterprise tool.

## Current State Analysis
- **Data:** Flat JSON files (`sop.json`, `notes.json`, `flags.json`).
- **Pipeline:** Linear script (`pipeline.py`) using `ThreadPoolExecutor` for concurrency.
- **Matching:** Basic TF-IDF-like keyword overlap in `matcher.py`.
- **Judgment:** Single-prompt AI call in `judge.py` with basic JSON parsing.
- **Frontend:** Streamlit app (`app.py`) reading static JSON files.
- **Logging/Error Handling:** Heavy use of `print` and basic `try-except` blocks.

---

## Phase 1: Core Infrastructure & Scalability
**Goal:** Move from static files to a scalable API and Database architecture.

### 1.1 Database Migration
- **Replace:** `backend/data/*.json` $\rightarrow$ **PostgreSQL**.
- **Library:** `SQLAlchemy` (ORM) + `Alembic` (Migrations).
- **Schema Design:**
    - `Plants`: `id, name, location, config`
    - `SOPs`: `id, plant_id, version, title, content, created_at`
    - `SOPSteps`: `id, sop_id, step_number, title, text`
    - `ShiftNotes`: `id, plant_id, date, shift, worker_id, text`
    - `DriftFlags`: `id, note_id, step_id, drift_type, quote, confidence, status (pending/approved/rejected), approved_by, approved_at`
    - `AuditTrail`: `id, flag_id, user_id, action, timestamp, comment`

### 1.2 API Transition
- **Replace:** `backend/src/pipeline.py` (as a script) $\rightarrow$ **FastAPI**.
- **Architecture:**
    - `/ingest`: Endpoints to upload SOPs and Shift Notes.
    - `/analyze`: Trigger the drift detection pipeline for a specific plant/date range.
    - `/flags`: CRUD operations for reviewing and updating flags.
    - `/config`: Manage "Drift Types" and model settings.
- **Validation:** Use `Pydantic` for all request/response models.

### 1.3 Operational Excellence
- **Logging:** Replace `print` with `structlog` or Python `logging` configured for JSON output (for ELK/Splunk).
- **Error Handling:** Implement a global exception handler in FastAPI and specific retry logic for AI calls (using `tenacity`).
- **Observability:** Add a dashboard for "Notes processed per minute" and "AI failure rates."

**Verification:**
- API endpoints return correct Pydantic-validated responses.
- Data persists across restarts in PostgreSQL.
- Log files show structured JSON entries.

---

## Phase 2: AI & Pipeline Robustness
**Goal:** Improve retrieval accuracy and judgment quality.

### 2.1 Advanced Retrieval (RAG)
- **Replace:** `backend/src/stages/matcher.py` (Keyword overlap) $\rightarrow$ **Vector Embeddings**.
- **Library:** `LangChain` or `LlamaIndex` + `pgvector` (PostgreSQL extension).
- **Mechanism:**
    - Embed SOP steps into a vector space.
    - Embed the shift note and perform a cosine similarity search to find the top $N$ relevant steps.
    - This handles synonyms (e.g., "isolator" vs "barrier") that keyword matching misses.

### 2.2 Enhanced Judgment
- **Modify:** `backend/src/stages/judge.py`.
- **Prompt Engineering:**
    - Implement **Few-Shot Prompting**: Include 3-5 "Gold Standard" examples of drift vs. no-drift.
    - **Structured Output:** Use OpenAI Tool Calling or JSON Mode to guarantee schema adherence, replacing the custom `parse_reply` logic.
    - **Chain-of-Thought:** Ask the model to explain its reasoning *before* providing the JSON list to improve accuracy.

### 2.3 Human-in-the-Loop (HITL)
- **Mechanism:**
    - When a user approves/rejects a flag in the frontend, store this in the `DriftFlags` table.
    - **Feedback Loop:** Periodically sample approved/rejected flags to create a new "Gold Standard" dataset for few-shot prompting.

**Verification:**
- Compare Matcher recall (Vector vs. Keyword) using the benchmark suite.
- Measure Judge precision/recall against the `answer_key.json` (gold standard).
- Verify that user approvals in the UI update the DB status.

---

## Phase 3: Enterprise Features
**Goal:** Add security, versioning, and industrial configuration.

### 3.1 Auth & RBAC
- **Security:** Implement `OAuth2` with `JWT` (JSON Web Tokens).
- **Roles:**
    - `Admin`: Manage plants, SOPs, and users.
    - `Reviewer`: Approve/Reject drift flags.
    - `Viewer`: Read-only access to analytics.

### 3.2 SOP Versioning
- **Mechanism:**
    - SOPs are never deleted; new versions are created.
    - The pipeline must use the SOP version that was active on the `date` of the shift note.
    - Add `valid_from` and `valid_to` columns to the `SOPs` table.

### 3.3 Industry-Specific Configuration
- **Mechanism:**
    - Move `DRIFT_TYPES` from hardcoded lists in `judge.py` to a database table `DriftTypeConfig`.
    - Allow admins to add/remove drift types based on the plant's industry (e.g., adding "safety_violation" for chemical plants).

**Verification:**
- Attempt to access `/analyze` without a token (should fail 401).
- Change a role from `Reviewer` to `Viewer` and verify the "Approve" button disappears.
- Run analysis on a note from 2025 and verify it uses the 2025 version of the SOP.

---

## Summary of Library Replacements

| Component | Hackathon Implementation | Professional Replacement |
| :--- | :--- | :--- |
| **Database** | `json.dump` / `json.load` | `PostgreSQL` + `SQLAlchemy` |
| **API** | Command-line arguments | `FastAPI` + `Pydantic` |
| **Matching** | Keyword Overlap (`matcher.py`) | `pgvector` + `LangChain` (Embeddings) |
| **AI Client** | `requests.post` (Manual) | `LangChain` / `OpenAI SDK` |
| **Logging** | `print()` | `structlog` / `logging` |
| **Validation** | `is_valid_proposal()` (Manual) | `Pydantic` models |
| **Auth** | None | `PyJWT` + `Passlib` |
| **Retries** | `for _ in range(self.retries)` | `tenacity` |

## Critical Files for Implementation
- `backend/src/pipeline.py` $\rightarrow$ Transition to FastAPI app.
- `backend/src/stages/matcher.py` $\rightarrow$ Implement Vector Search.
- `backend/src/stages/judge.py` $\rightarrow$ Structured outputs & Few-shot prompts.
- `backend/src/config.py` $\rightarrow$ DB connection strings & Env vars.
- `frontend/src/app.py` $\rightarrow$ Update to call REST API instead of reading local files.
