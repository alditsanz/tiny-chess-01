# Tiny Chess — tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/alditsanz/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/alditsanz/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 3,720 bytes of Python (`main.py`). It plays the house
gauntlet through the env: `POST /game` serves the game in play, `POST /move`
plays a UCI move, and the loop ends when the env answers `done`.

## The engine

- 0x88 board, legal move generation (castling, en passant, promotion),
  check / checkmate / stalemate handled by the search.
- Negamax alpha-beta with a transposition table, MVV-LVA + killer-move +
  history ordering, null-move pruning, late-move reduction, and a
  quiescence search over captures, promotions and replies to check
  (capped so perpetual-check lines cannot run away). Move legality is
  checked lazily at search time, not at generation time, which makes
  the search about a third faster at the same node budget.
- Evaluation: material (pawn 100, knight 320, bishop 330, rook 500,
  queen 900) plus piece-square tables, updated incrementally as moves are
  made, so no full-board scan is needed inside the search.
- Iterative deepening to a fixed budget of 140,000 nodes a move —
  deterministic, no clock, no unseeded randomness, so a replay plays the
  same moves. Worst observed move on one CPU is about 3.5 seconds, inside
  the 10-second move limit.
- The readable source (6,909 bytes) is packed as a zlib + base85 payload
  with its unpacker, as the rules allow; the payload and the unpacker both
  count toward the 4,096-byte cap. The unpacked source is the engine.

## Local test

Run the kit's env server against a practice trial, then the engine:

```sh
MAKEFUN_ENV_DATA_DIR=<kit>/practice/trial-0/input/env \
MAKEFUN_STATE_DIR=/tmp/tc-env MAKEFUN_ENV_PORT=8081 \
  node <kit>/program/env/server.mjs
MAKEFUN_ENV_URL=http://127.0.0.1:8081 python3 main.py
```

Move generation is verified against the standard perft suite
(start position depth 4: 197,281) and the incremental evaluation is
checked against a full-board evaluation over random games.
