#!/bin/zsh
# Picks each language's moments once its 1 v 1 recording is logged as done.
cd /tmp/sitecap
done_langs=""
while true; do
  for L in $(grep -h "headsUp recorded" run1.log run2.log | awk '{print $1}'); do
    if [[ " $done_langs " != *" $L "* ]]; then
      python3 pick.py $L >> picks.log 2>&1
      done_langs="$done_langs $L"
    fi
  done
  [[ $(echo $done_langs | wc -w) -ge 17 ]] && break
  sleep 20
done
echo ALLDONE >> picks.log
