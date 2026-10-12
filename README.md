# TrailTruth

**A hiking assistant that is not allowed to make things up.**

TrailTruth is a phone app for hikers. The whole park, meaning trails, water, elevation, roads and landmarks, downloads to your phone, so it works with no signal. It answers the questions people actually ask on a trail ("where am I?", "how do I get out?", "is there water near me?", "when does it get dark?") from official government map data only. When it doesn't know something, it says so.

![TrailTruth on a phone](img/main.png)

![Asking whether a trail is too hard for the kids](media/ask.gif)

## Why

Search and rescue teams have been pulling people off mountains after a chatbot or a street-map app gave them a confident, wrong answer. Gemini told three hikers on Mount Shasta to pack far less food and water than they needed. ChatGPT sent two hikers in Poland's Tatra Mountains over a "shortcut" into climbing terrain. Google Maps told three teenagers a trail would take 5 hours and 13 minutes when it takes 8 to 14. The sourced cases are in [RESCUES.md](RESCUES.md).

TrailTruth is built the other way round. The map data answers, and the AI only gets to talk about what the data already proved.

## What it does

- **Where am I.** The trail you're on, which way you're facing, and how far it is to the next junction or road.
- **The way out.** The shortest mapped route back to a road or trailhead, with distance, climb and time.
- **Water.** Mapped springs, streams, lakes and taps near you, and whether a stream runs all year. It can't tell you if water is flowing today, and it says so.
- **Daylight.** Sunset where you are standing, and how much light you have left.
- **Trip planner.** Day-by-day legs, camps, water and exits.
- **Emergency.** One tap shows 911 first, then your coordinates in three formats including the US National Grid rescuers use, then the nearest places a rescuer can reach.
- **Park passport and achievements.** Walk up to real summits, waterfalls and viewpoints to stamp them. Earn achievements for miles, climb and steps, all measured by the phone.
- **Trail companion (optional).** A small AI model (Gemma 3 1B) that runs on the phone itself. Every name, number and direction it says is checked against the map before you see it. A line it can't back up is cut, and it tells you it left something out. In an emergency it is skipped entirely.

## Where it works

261 downloadable areas in 41 states and 2 territories: national parks, state parks, national forests (big ones split into sections that fit on a phone), wilderness areas, seashores and parkways. **Free Walk** works anywhere, even from your front door: the GPS draws your walk on a USGS topo map, and every saved walk becomes part of your own map layer.

## How it stays honest

1. Every answer is computed from the map data on the phone.
2. A checker reads the final words and rejects any distance, name, direction or claim the data didn't produce.
3. If it doesn't know (weather, closures today, snow, how hard a hike is for you), it says so and shows the facts it does have.
4. With signal, it shows National Weather Service and National Park Service alerts word for word, with their source.

These checks (more than 7,000) run on all 261 areas before every release: calls for help asked many different ways at many spots in each park (always answered with 911 first, never dodged), routes checked against the true shortest path, planted lies that the checker has to catch, and questions the data cannot answer.

## The companion, tested blind against Claude

Gemma 3 1B was fine-tuned on answers written by code from the map data (never by another AI), then tested on 80 fresh questions from 14 parks it never trained on. The same questions, map facts and checker were used for every model, and the answers were graded blind against a written rubric.

| 80 blind questions, 14 unseen parks | made something up | useful on its own |
|---|---|---|
| stock Gemma 3 1B | 47 / 80 | 29 / 80 |
| fine-tuned Gemma 3 1B (round 4) | 10 / 80 | 59 / 80 |
| fine-tuned Gemma 3 1B (round 4) + three new checks | 2 / 80 | 54 / 80 |
| Claude Haiku | 1 / 80 | 70 / 80 |
| Claude Sonnet | 3 / 80 | 69 / 80 |
| Claude Opus | 0 / 80 | 72 / 80 |

A Claude grader read every answer. Because a Claude model grading Claude is a conflict, OpenAI's Codex graded them too: the two agreed on "made something up or not" 95% of the time. The full write-up is in the DEV post.

## What's open, and what isn't

This repository is a showcase: the write-up, screenshots, demo GIFs and sources. The app code, data pipeline, test suite and trained model are not published here.

## Data and credits

- Trails, roads and boundaries: USGS National Map, National Park Service, USGS PAD-US
- Elevation: USGS 3D Elevation Program
- Water: USGS National Hydrography Dataset
- Place names: USGS GNIS
- Community paths: © OpenStreetMap contributors (ODbL), via Overture Maps
- Weather and alerts: National Weather Service, National Park Service
- On-phone AI: Google Gemma 3 1B, run in the browser with WebLLM (MLC)
- QR codes: qrcode-generator by Kazuhiko Arase (MIT)

**Not your only navigation.** Carry a paper map and compass, tell someone your plan, and check the park's alerts before you go.

Built with AI coding help (Claude).
