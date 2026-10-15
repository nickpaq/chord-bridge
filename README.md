# Chord Bridge

Open Chord Bridge.html in a desktop browser. No server, installation or internet required.
Select multiple Cthulhu .fxp files, choose a pad layout and velocity, then click Convert & download ZIP. Extract the ZIP and import its .chrd files into ChordPolyPad. Output filenames match input filenames with .fxp replaced by .chrd. Each valid input produces one output. Duplicate filenames are stored in separate duplicate-N folders, preserving their basenames. Unsupported files and conversion failures are skipped and listed with their errors. Valid files still download as a ZIP, with a total of exported and skipped files.

Supports the 8312-byte Cthulhu chord chunk layout identified by Nr8v, based on the supplied ADSR OVO CP001 C.fxp sample. Stores eight voice lanes across 128 trigger keys; nonzero note values are interpreted as MIDI note / 128. Zero represents an empty voice. Other layouts are rejected. The legacy outer FXP byteSize field in the sample is stale; the actual chunk size is validated instead.

Default layout packs assigned chords from pad 1. Keep MIDI positions places key 0 on pad 1, key 48 on pad 49, etc. Note names use MIDI 60 = C4. Velocity defaults to 100 and can be changed; original velocity, arpeggiator and modulation settings are not converted. No transposition or voice sorting is applied. Pad labels show the voicing, not guessed chord names.

Validation: supplied preset decoded as 48 chords, trigger keys 48–95. Both pad layouts and all note values independently checked with Python plistlib. 200-file ZIP tested with Python zipfile including CRC and Unicode filename checks. Browser interaction and import/playback in ChordPolyPad have not been tested here. Verify the first converted chord: MIDI notes 38, 60, 65, 69 (D2, C4, F4, A4).

Source: core.js, page.html. The standalone HTML embeds core.js. test.cjs accepts the original example .fxp path. No third-party dependencies.
