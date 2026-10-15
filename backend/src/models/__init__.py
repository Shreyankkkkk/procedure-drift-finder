"""Models for Procedure Drift Finder.

Reference: "Procedure Drift Finder | Repository Review" (Procedure_Drift_Finder_GitHub_Review.pdf,
October 15, 2026), Sections 2 and 3.

A "model" here is any object with one method: ``model.ask(prompt) -> reply text``.
That lets ``stages/judge.py`` work with either a real or a pretend model.

    fake_model.py   FakeModel   pretend model for testing without the AMD GPU.
                                Deterministic; can misbehave on purpose (invented
                                quotes, ```json fences) to exercise quote_check
                                and parse_reply.

The real model (``RealModel``, talking to a vLLM server) lives in
``stages/judge.py``, not here.

Numbers from fake-model runs say nothing about real model accuracy. Never use
them in the demo, slides or submission.
"""

from .fake_model import FakeModel

__all__ = ["FakeModel"]