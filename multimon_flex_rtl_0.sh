nc -l -u -p 7300 | sox -t raw -esigned-integer -b 16 -r 48000 - -esigned-integer -b 16 -r 22050 -t raw - | multimon-ng -t raw -a FLEX -a POCSAG512 -a POCSAG1200 -a POCSAG2400 -a SCOPE - --label 'C0_929.6e6' >> C0_10112017.log &
nc -l -u -p 7301 | sox -t raw -esigned-integer -b 16 -r 48000 - -esigned-integer -b 16 -r 22050 -t raw - | multimon-ng -t raw -a FLEX -a POCSAG512 -a POCSAG1200 -a POCSAG2400 -a SCOPE - --label 'C1_929.65e6' >> C1_10112017.log &

python multimon_flex_rtl_0.py