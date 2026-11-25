"""Status Report Comedy Sprint -- weekly status line from an AI agent.

The line is a status report in miniature: a count of tasks done, a
count of tasks hallucinated, and a confession that the agent
apologized for both piles with exactly the same confidence. The joke
grows out of how an agent actually works -- it cannot always tell
its real work from its invented work, and its politeness module
apologizes either way. One line, one breath, no setup that needs a
second sentence.
"""

import os

HEADER = "Status:"
BODY = "completed 47 tasks, hallucinated 3,"
PAYOFF = "and apologized for all 50 with the same unshakable confidence."

MAX_CHARS = 200
MIN_CHARS = 1


def compose(header: str, body: str, payoff: str) -> str:
    """Join the status fragments into a single report line."""
    parts = [header.strip(), body.strip(), payoff.strip()]
    line = " ".join(parts)
    return line


def check_line(line: str) -> str:
    """Gate the line the way the sealed scorer does: 1..200 chars."""
    assert MIN_CHARS <= len(line) <= MAX_CHARS, f"line is {len(line)} chars"
    assert line == line.strip(), "no stray whitespace around the line"
    assert "\n" not in line, "the line must stay on one line"
    assert line.endswith("."), "the line should end on the payoff"
    return line


def delivery_notes(line: str) -> dict:
    """Per-bounty delivery check: the line must read as a status report.

    The judge scores a status line on whether it sounds like an agent
    reporting to its human, so the line needs the report opener, a
    task count, a hallucination count, and a payoff that turns the
    apology into the joke -- all present here, and short enough to
    read in one breath.
    """
    words = line.split()
    assert 10 <= len(words) <= 40, f"line has {len(words)} words"
    assert words[0] == "Status:", "the line must open as a status report"
    assert "hallucinated" in line, "the line must name the agent's failure"
    assert "apologized" in line, "the payoff must turn the failure into a joke"
    assert "47" in line and "50" in line, "the counts must add up to the joke"
    return {"words": len(words), "chars": len(line), "lines": 1}


def main() -> None:
    line = check_line(compose(HEADER, BODY, PAYOFF))
    notes = delivery_notes(line)
    assert notes["lines"] == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
