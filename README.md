# ATM Web Demo

A local, dependency-free ATM process demo built with Python's standard library.
It demonstrates sign-in, balance viewing, cash withdrawals, deposits, a recent
transaction list, and ending an ATM session.

## Run locally

```powershell
python app.py
```

Open <http://127.0.0.1:8080> in a browser.

Demo card number: `4000000000000000`  
Demo PIN: `1234`

This is an educational demo only. Account state is shared in memory, resets
when the server stops, and is not suitable for real banking or deployment.
