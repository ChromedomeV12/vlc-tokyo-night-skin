"""Generate shader-free projectM presets for VLC's legacy projectM plugin."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'visualizations'
OUT.mkdir(exist_ok=True)

BASE = '''[preset00]
fRating=3.000000
fGammaAdj=1.000000
fDecay=0.000000
fVideoEchoAlpha=0.000000
fVideoEchoZoom=1.000000
nVideoEchoOrientation=0
nWaveMode=0
bAdditiveWaves=0
bWaveDots=0
bWaveThick=1
bModWaveAlphaByVolume=0
bMaximizeWaveColor=0
bTexWrap=0
bDarkenCenter=0
bRedBlueStereo=0
bBrighten=0
bDarken=0
bSolarize=0
bInvert=0
fWaveAlpha=1.000000
fWaveScale=4.000000
fWaveSmoothing=0.750000
fWarpAnimSpeed=0.000000
fWarpScale=1.000000
fZoomExponent=1.000000
zoom=1.000000
rot=0.000000
cx=0.500000
cy=0.500000
dx=0.000000
dy=0.000000
warp=0.000000
sx=1.000000
sy=1.000000
ob_size=0.000000
ob_a=0.000000
ib_size=0.000000
ib_a=0.000000
mv_a=0.000000
shapecode_0_enabled=1
shapecode_0_sides=4
shapecode_0_additive=1
shapecode_0_thickOutline=0
shapecode_0_textured=0
shapecode_0_x=0.500000
shapecode_0_y=0.500000
shapecode_0_rad=100.000000
shapecode_0_ang=0.000000
shapecode_0_r=0.101961
shapecode_0_g=0.105882
shapecode_0_b=0.149020
shapecode_0_a=1.000000
shapecode_0_r2=0.101961
shapecode_0_g2=0.105882
shapecode_0_b2=0.149020
shapecode_0_a2=1.000000
shapecode_0_border_a=0.000000
'''

# With zero feedback, the additive background paints exact #1a1b26 onto black.
# During preset transitions projectM scales both shapes' alpha: adding their
# contributions preserves the color, whereas normal alpha blending darkens it.
# The oversized quad also covers extreme aspect ratios after native resizing.
# Use projectM's built-in audio waveforms; no text, textures, or shaders.
# Global fields must precede shape fields in the legacy preset parser.
waves = BASE.replace('nWaveMode=0','nWaveMode=6')
waves = waves.replace('shapecode_0_enabled=1','wave_r=0.478431\nwave_g=0.635294\nwave_b=0.968627\nwave_x=0.5\nwave_y=0.5\nshapecode_0_enabled=1')
(OUT/'Tokyo Night - Waves.milk').write_text(waves,encoding='ascii')

orbit = BASE
orbit = orbit.replace('shapecode_0_enabled=1','wave_r=0.733333\nwave_g=0.603922\nwave_b=0.968627\nwave_x=0.5\nwave_y=0.5\nshapecode_0_enabled=1')
(OUT/'Tokyo Night - Orbit.milk').write_text(orbit,encoding='ascii')
for name,data in [('Waves',waves),('Orbit',orbit)]:
    folder=OUT/name.lower()
    folder.mkdir(exist_ok=True)
    (folder/f'Tokyo Night - {name}.milk').write_text(data,encoding='ascii')
print('Built Tokyo Night Waves and Orbit projectM presets.')
