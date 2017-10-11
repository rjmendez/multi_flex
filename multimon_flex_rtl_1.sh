nc -l -u -p 7306 | sox -t raw -esigned-integer -b 16 -r 48000 - -esigned-integer -b 16 -r 22050 -t raw - | multimon-ng -t raw -a FLEX -a POCSAG512 -a POCSAG1200 -a POCSAG2400 -a SCOPE - --label 'C6_931.5e6' >> C6_10112017.log &
nc -l -u -p 7307 | sox -t raw -esigned-integer -b 16 -r 48000 - -esigned-integer -b 16 -r 22050 -t raw - | multimon-ng -t raw -a FLEX -a POCSAG512 -a POCSAG1200 -a POCSAG2400 -a SCOPE - --label 'C7_931.85e6' >> C7_10112017.log &

python multimon_flex_rtl_1.py