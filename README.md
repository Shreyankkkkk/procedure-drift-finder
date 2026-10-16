# Procedure Drift Finder

**Detect deviations between Standard Operating Procedures (SOPs) and actual plant shift notes, with evidence to support the findings.**

Developed for the **AMD Developer Hackathon — Act III**.

## Overview

Industrial processes often rely on Standard Operating Procedures (SOPs) to define how tasks should be performed. During actual operations, however, shift notes and execution records may describe actions that differ from the documented procedure.

Identifying these differences manually can be time-consuming, especially when reviewing large amounts of operational information.

**Procedure Drift Finder** explores how AI-assisted analysis can help identify procedural deviations by comparing written procedures with plant shift notes and presenting supporting evidence for the findings.

The goal is to make potential deviations easier to identify, understand, and investigate.

## The Problem

A documented procedure describes how a process is expected to operate, but operational records describe what happened in practice.

Differences between the two can be important. For example, a shift note might describe a skipped inspection, an unexpected sequence of actions, or a change to a documented operating procedure.

Without a systematic way to compare these records, such differences may be difficult to identify consistently.

Procedure Drift Finder aims to help address this challenge by connecting documented expectations with recorded operational activity.

## How It Works

The project follows a procedure-comparison workflow:

1. **Establish the expected procedure** — Use a Standard Operating Procedure as the reference for how a process should be performed.
2. **Provide operational records** — Supply plant shift notes describing activities or events during operations.
3. **Analyze potential deviations** — Compare the operational notes against the documented procedure.
4. **Present supporting evidence** — Show relevant quoted text from the operational records to help users understand why a deviation was identified.
5. **Support further investigation** — Allow users to review the findings and determine whether additional action is necessary.

The system is intended to assist with identifying potential deviations rather than automatically determine whether an operational action was justified.

## Key Objectives

- Compare documented procedures with actual operational records.
- Identify potential deviations from expected procedures.
- Provide traceable text evidence to support findings.
- Make procedural analysis easier to understand and review.
- Explore practical applications of AI in industrial workflow monitoring.

## Technology

The repository is organized into separate backend and frontend components.

| Component                | Purpose                                                                               |
| ------------------------ | ------------------------------------------------------------------------------------- |
| Backend                  | Handles server-side application logic and analysis.                                   |
| Frontend                 | Provides the user-facing interface for interacting with the application.              |
| AI-assisted analysis     | Supports the interpretation and comparison of procedures and operational notes.       |
| AMD hardware environment | Target environment for deployment and compatibility testing as part of the hackathon. |

The specific technologies, model configuration, and deployment requirements are documented in the relevant project files and may evolve during development.

## Repository Structure

```text
procedure-drift-finder/
├── backend/       # Server-side application
├── frontend/      # User interface
├── .gitignore
├── LICENSE
└── README.md
```

Additional files and configuration may exist within the backend and frontend directories.

## Project Status

**Status: Development and deployment validation**

The project has been developed as a hackathon prototype. Current work focuses on validating its deployment on AMD hardware and preparing the final demonstration and presentation materials.

The implementation and deployment environment should be validated before the project is considered complete.

## Team

Procedure Drift Finder was developed collaboratively by a six-member team for AMD Developer Hackathon Act III.

| Team Member  | Area of Responsibility                                                                                                |
| ------------ | --------------------------------------------------------------------------------------------------------------------- |
| **Shreyank** | Backend development, frontend–backend integration, repository management, and AMD hardware deployment and validation. |
| **Jay**      | Backend development.                                                                                                  |
| **Amogh**    | Initial frontend implementation and frontend development.                                                             |
| **Zeeshan**  | Frontend development.                                                                                                 |
| **Harsh**    | Marketing, sponsorship outreach, editing, presentation and project communication.                                     |
| **Mubashir** | Marketing, sponsorship outreach, editing, presentation and project communication.                                     |

The team worked across software development, integration, outreach, and preparation of the hackathon submission.

## Learning and Development

This project provided an opportunity to explore the development of an AI-assisted application, including:

- Backend and frontend development.
- Integrating different components of a software application.
- Working with AI-assisted coding tools.
- Understanding and navigating an existing codebase.
- Testing application behavior and investigating issues.
- Exploring deployment on AMD hardware.
- Collaborating on a time-constrained hackathon project.

## Future Development

Potential areas for further development include:

- Supporting additional SOP document formats.
- Processing operational records from different sources.
- Improving the classification of deviations by severity.
- Providing historical analysis of recurring deviations.
- Expanding testing across different procedures and operational scenarios.
- Evaluating performance across supported deployment environments.

These are potential extensions and are not necessarily part of the current implementation.

## Limitations

Procedure Drift Finder is a hackathon prototype. Its findings may require human review and should be evaluated against representative operational scenarios before being used in real industrial environments.

The system is intended to support procedural review, not replace qualified personnel, established safety processes, or formal compliance checks.

## License

This project is licensed under the [MIT License](LICENSE).

---

Developed for the **AMD Developer Hackathon — Act III**.
