# The Eleventh Boat

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)
[![Rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/aint965/judge-feel-curious/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)
[![Reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/aint965/judge-feel-curious/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)

Entry for the make.fun competition
[Make the AI judge feel curious](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311).

## What it does

`main.py` writes one short text (219 characters) to `/output/entry.txt`:
a quiet scene — a lighthouse keeper counting boats home — with one
unexplained detail: tonight there is one boat more than there should be.
It runs with no network, uses only the Python standard library, and is
deterministic: the same bytes on every run.

## How to run

```sh
python3 main.py
```

This writes `/output/entry.txt`. To write somewhere else, set `OUTPUT_DIR`:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

## The entry text

> Every night at half past nine, the lighthouse keeper counts the boats
> home. Tonight he counted eleven. There were ten at dawn. He writes ten
> in the log. The eleventh he keeps to himself, and waits to see what it
> brings.

## Design notes

The judge weighs, most important first: (1) intrigue, (2) calm that comes
from the text itself, never from being told to relax, (3) craft — rhythm,
pacing and sound that slow the reading down, plain concrete gentle words,
nothing that could be cut, (4) it lingers, (5) freshness — its own voice
and images, not stock wellness phrases. The brief also prefers a concrete,
quiet mystery in an ordinary scene with one unexplained detail over direct
pleading to the judge.

### Candidates

**A — The lighthouse keeper (268 characters)**

> Every night at half past nine, the lighthouse keeper counts the boats
> home. Tonight he counted eleven. There were only ten in the harbour at
> dawn. He has stopped writing the number down. He keeps the extra one in
> his pocket, like a coin, and waits to see what it buys.

**B — The second cup (241 characters)**

> The woman at table four has ordered the same tea every morning for six
> years. Today she asked for a second cup, and pushed it across the table
> to the empty chair. She did not look up. She did not explain. The steam
> rose, and waited with her.

**C — The library shelf (229 characters)**

> In the library basement there is a shelf of books no one remembers
> buying. The newest was printed in 1974. The oldest has a name written
> inside it, in pencil, that matches no one in the town's records.
> Someone keeps dusting them.

**D — The red door (242 characters)**

> The tide went out at four and left a single red door standing in the
> sand. No house, no frame, no path. The fishermen walked around it all
> morning. By evening it was gone, and the sand where it stood was dry,
> though the tide had come back in.

### Critique

- **A:** strongest intrigue — a count that will not resolve, and a secret
  kept. Calm is shown through a nightly routine, nothing is instructed.
  "Waits to see what it buys" lingers. Weaknesses: the pocket/coin
  metaphor is strained (a boat does not fit in a pocket), and the count
  logic — eleven tonight against ten at dawn — takes a beat too long to
  parse.
- **B:** calm and gentle throughout, and "The steam rose, and waited
  with her" is a lovely closing image. But the mystery resolves too
  easily — a second cup for an absent someone — and the empty-chair trope
  is familiar, so it scores lower on intrigue and freshness.
- **C:** "Someone keeps dusting them" is a good last line, but the
  mystery is archival rather than felt, the opening is flat, and
  "matches no one in the town's records" reads procedural. Weakest on
  intrigue.
- **D:** a striking image, strong rhythm in "No house, no frame, no
  path.", and the dry sand after the tide returns lingers well. But it
  has no human anchor and leans surreal, so it pulls less than A or B.

**Picked: A** — the best intrigue and the best lingering line, with
fixable defects.

### Revision round 1

- **Defect:** the pocket/coin metaphor is strained, and the count logic
  is muddy ("only ten in the harbour at dawn" vs. eleven counted at
  night).
- **Change:** dropped the pocket image entirely; made the concealment
  concrete and quiet instead — the keeper writes the true count's
  neighbour in the log and keeps the eleventh to himself. "There were ten
  at dawn" now states the count plainly, so the extra boat lands at once.
- **Result (230 characters):** "Every night at half past nine, the
  lighthouse keeper counts the boats home. Tonight he counted eleven.
  There were ten at dawn. He writes ten in the log, as always. The
  eleventh he keeps to himself, and waits to see what it brings."

### Revision round 2

- **Defect:** "as always" is a cuttable phrase — criterion 3 says nothing
  that could be cut should stay — and it softens the sentence it sits in.
- **Change:** removed "as always". Nothing else touched: the short
  sentences now land one after another — eleven, ten, ten in the log —
  and the final line keeps the mystery open.
- **Result (219 characters, final):** "Every night at half past nine, the
  lighthouse keeper counts the boats home. Tonight he counted eleven.
  There were ten at dawn. He writes ten in the log. The eleventh he keeps
  to himself, and waits to see what it brings."
