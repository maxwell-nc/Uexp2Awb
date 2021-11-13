# Uexp2Awb
extract unpack asset file (form unreal engine 4 pak) with extenstion *.uexp which contain awb/acb (cri/cpk like) sound or music resource.
i just check it work well with one music game(id*m*s_s*s) use ue4.24 and one rpg game(p*l7) use ue4.25.
you can just read src and translate into quickbms script.

# Usage
just put script into your uexp file folder, then run
```bash
python uexp2awb.py
```
it will auto transform all the file under current folder, ex: file.uexp to file.uexp.awb.
