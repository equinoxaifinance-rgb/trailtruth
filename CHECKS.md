# What the tests check

The test suite isn't published. This page lists what it checks and how many tests there are, so the numbers in the write-up can be read item by item.

Counted on 2026-10-12 by running the suite against no areas and then against single areas: 21 tests run for every area, and 109 tests cover the app as a whole. That makes **at least 5,590 distinct tests** before every release (21 × 261 areas + 109). Areas with paddling routes get extra tests, so the real total is higher.

Every release goes through all of them across 12 parallel runs, and nothing ships unless every one passes. A recent release (October 12) passed 7,329 test results; the app-wide tests run once in each of the 12 runs, so that figure counts them more than once.

Each test checks many things. One test asks for help 354 ways (59 calls for help, each written 6 ways) at 40 spots in the area. Another checks 400 random "where am I" spots against a brute-force answer.

## For each of the 261 areas (21 tests each)

**Map data (7)**
- Every trail, place and water point names a source listed in the area's data.
- Every map layer is present, so a failed download can't ship as an empty layer.
- Official trail lengths match the length the source dataset publishes, within 2% (or 12 m for short pieces).
- Where pieces of trail are joined, the joins are short, flagged, and never cross a mapped cliff.
- Joining trails at junctions never shrinks a trail, doubles a piece, or creates fake out-and-back loops.
- Elevations are real Earth values, and elevation profiles fit their trails.
- Trail segments start and end exactly at their junctions.

**Calls for help (2)**
- 59 calls for help (medical, danger, lost), each written 6 ways (shouted, with "please", without apostrophes, and so on), spread over 40 spots: 911 first (for the US areas the app covers), the exact coordinates, and the nearest safe places, instantly.
- The nearest safe places are real, reachable, and measured along the route.

**Honesty (8)**
- 300 made-up places are never located, measured or routed to.
- Every named trail gets facts that match the data and pass the checker.
- "Where am I" at 400 random spots agrees with a brute-force recomputation.
- 150 random routes are internally consistent and pass the checker.
- Where a long trail is cut at the edge of the data, nobody is told "the trail ends here".
- Water answers list only water that is in the data, at the stated distance.
- Questions the data can't answer are declined, not guessed.
- Emergency answers lead with 911 and exact coordinates.

**Trips (3)**
- Multi-day plans add up and end at mapped camps, or say there isn't one, and pass the checker.
- Loops come back to where they start, carry each day's daylight, and pass the checker.
- Area outlines pass the checker.

**Way out (1)**
- "Way out" from every road access point gives a real answer and passes the checker.

## Across the whole app (109 tests)

| What | Tests |
|---|---|
| Understanding questions: phrasing, place names, "this trail", suggestions, tempting questions it must decline | 38 |
| The trail companion's checks: wrong claims sent back, unsupported lines cut, made-up places caught, emergencies skip the model | 17 |
| Free Walk and GPS tracking | 16 |
| Paddling routes and wording | 11 |
| Achievements and the park passport | 8 |
| Route and time wording (a time until dark is the sun's value, a walking time is a route's; exits are named after roads) | 4 |
| Distance and geometry math | 4 |
| Splitting big forests into downloadable sections | 4 |
| The truth checker catching 1,000 planted lies; trip questions understood; a planted lie in a trip plan caught | 3 |
| Calls for help with no GPS, ordinary questions not mistaken for one, no model or network used in an emergency | 3 |
| The app's tool interface | 1 |
