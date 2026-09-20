# Project TODO

## Current priority: performance and compatibility

- [x] Replace tiny background tiles that caused excessive drawing during resize.
- [x] Remove the redundant idle background layer.
- [x] Check player and playlist resizing, maximize/restore, and seek-bar alignment in VLC.
- [ ] Confirm resize responsiveness in normal use after reloading the optimized skin.
- Prefer VLC's existing controls, dialogs, menus, and rendering features. Preserve the horizontal menu row.

## Later: simple DJ features

- [ ] Investigate track-to-track crossfades and simple transitions, clearly separating native VLC features from features that need a companion tool.
- [ ] Expose or document VLC's native equalizer for bass boost.
- [ ] Investigate timed track switches and per-track start/stop points.
- [ ] Assess a two-player companion or a dedicated DJ application if native VLC cannot provide reliable mixing; do not burden the skin with an untested playback engine.

## Later: audio visualization customization

- [ ] Add Tokyo Night blue/purple visualizations on the dark background, without branding, captions, or emojis.
- [ ] Prefer the installed projectM plugin and compatible presets; validate loading, audio response, embedding, and performance in VLC before shipping.
- [ ] Add documented preset selection and customization, with an easy return to VLC's default visualization settings.

DJ and visualization work is deferred until the current optimization work is settled.
