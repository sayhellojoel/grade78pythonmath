# Project: Flappy Rhema (PWA)
Target: Single-shot build for a Grade 8 "Vibe Coding" demo.
Host: Netlify (Private Repo)

## Technical Stack & Constraints
- Framework: React (Vite) with TypeScript.
- Styling: Tailwind CSS.
- Animations: Framer Motion for bird physics, obstacle movement, and retro explosions.
- PWA: Generate a manifest.json and a Service Worker for offline play and "Add to Home Screen."
- Responsiveness: Must work perfectly on Chromebooks (keyboard) and Mobile (touch).
- Build Step: Before finishing, verify the project builds with `npm run build`.

## Game Logic: Flappy Bird Core
- A yellow bird falls continuously due to gravity. The player taps/clicks or presses Spacebar to make the bird flap upward.
- Candy cane obstacles scroll in from the right in pairs (one top, one bottom) with a gap in the middle for the bird to fly through.
- The bird must pass through the gap without touching the candy canes, the top of the screen, or the bottom of the screen.
- If the bird collides with anything, a life is lost.
- The game area occupies the full screen between the top score/lives banner and the bottom control bar.
- The bird starts centered vertically on the left third of the screen. The game does not start until the first tap/spacebar press.

## Candy Cane Obstacles
- Render candy canes as vertical striped red-and-white poles with a classic curved candy cane hook at the top of the bottom cane and at the bottom of the top cane (pointing toward the gap).
- Obstacle pairs spawn off the right edge and scroll left at a consistent speed.
- Gap size: Start at a generous gap (≈40% of game height). Narrow slightly as the score increases, using a diminishing curve so it never becomes literally impossible.
- Progression: Scrolling speed also increases with score using a logarithmic curve:
  - Early game: slow and forgiving.
  - After 20 points: noticeably faster but still passable.
- Horizontal spacing between obstacle pairs should also tighten gradually.

## Point Collector (Rhema Logo)
- Place the Rhema Christian School logo as a small circular coin/badge centered in the gap of every candy cane pair.
- When the bird flies through the gap and passes the logo, it is "collected" — animate it with a quick scale-up + fade-out burst effect and award 1 point.
- Use the image file `public/rhema-logo.png` for the logo. (Provide this file separately — drop it into the public folder before running the build.)

## Lives & Collision
- Lives: 3 lives. Lose a life if:
  1. The bird touches a candy cane.
  2. The bird touches the top or bottom boundary of the game area.
- Life Loss Event: On life loss, pause the game for 2 seconds. Show a high-quality retro pixel-art explosion animation at the bird's position. After the explosion, reset the bird to its starting position and resume.
- If all 3 lives are lost, the game ends and the "Game Over" screen is shown.

## Controls
- Desktop: Spacebar to flap.
- Mobile: Tap anywhere on the game area to flap.
- A clearly visible "TAP TO START / PRESS SPACE TO START" message should appear on the start screen and after each life-loss reset.

## Scoring & High Scores
- 1 point per candy cane pair successfully passed (logo collected).
- High Scores: Save to `localStorage`. Store: Score (integer), Name (up to 15 characters), and Theme (skin name).
- Keep the top 10 scores, sorted by score descending.
- Show the High Scores screen when the player clicks "High Scores" from the main menu.

## Retro Skins (Themes)
User selects a theme from the main menu (Default: Plain). Theme persists for the entire session — even after game over, the theme stays selected.

1. **"Plain"**: Atari-style, black background, green "phosphor" text, blocky pixel explosions. Candy canes are pixel-art style.
2. **"Fairy Princess"**: Pink/purple sky background with floating sparkles, pastel candy canes, heart-shaped explosion on collision, soft sparkle sound.
3. **"Spaceship"**: Dark blue starfield background, neon/techy font, candy canes with a neon glow outline, fiery explosion on collision, ship-thruster ambient sound.

## UI Screens
1. **Start Screen**: Game title ("Flappy Rhema"), Mode/Theme selector, High Scores button, and a Start button.
2. **Game Screen**: Top banner (score, lives as heart icons, current theme label). Game area fills the rest. On mobile, a subtle "Tap to Flap" hint fades out after the first tap.
3. **Game Over Screen**: Final score, "Enter Your Name" input (max 15 chars), Submit Score button, Play Again button, Main Menu button.
4. **High Scores Screen**: Top 10 local scores from `localStorage`, showing rank, name, score, and theme.

## Implementation Instructions (Agent Only)
1. Create a `src/components/` folder for: `GameBoard`, `Bird`, `CandyCanePair`, `RhemaLogo`, `ScoreBoard`, `ExplosionEffect`, and `NumberPad` (for mobile flap button if needed).
2. Implement a `useGameLoop` custom hook using `requestAnimationFrame` to handle physics, collision detection, and obstacle scrolling.
3. Implement a `useFlappyPhysics` hook to manage bird Y position, velocity, and gravity constants.
4. Candy cane gap center Y position should be randomized within a safe range each time a new pair spawns (not too close to top or bottom edge).
5. Division/collision logic: use bounding-box collision detection. Bird hitbox should be slightly smaller than the visual bird for fairness.
6. Setup `vite-plugin-pwa` to handle PWA requirements automatically.
7. Use the 'Press Start 2P' Google Font for all UI text.
8. Only one candy cane pair should be on screen at a time in early game. As score increases, allow a second pair to be on screen simultaneously once the spacing tightens.

## Additional Details & Requirements
1. The game area top boundary is the bottom edge of the score/lives banner. The game area bottom boundary is the top edge of any bottom control bar (or the bottom of the screen on desktop).
2. When a life is lost, the bird and candy canes freeze in place immediately. The explosion plays at the bird's position. After the 2-second explosion, the candy canes reset (clear the screen) and the bird resets to starting position. The next round begins on the next tap/spacebar.
3. Do not clear the screen until the explosion animation fully completes.
4. The Rhema logo coin should only be visible while the candy cane pair is active on screen. Once collected or once the pair exits the screen, the logo disappears.
5. Theme selection on the main menu must persist in React state so that returning to the main menu after a game does not reset the theme.
