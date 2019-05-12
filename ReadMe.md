# Star Tracker

Control of a stepper motor for a "Barn Door Tracker"

## Sequence on GPIO ports

Full step mode

| GPIO17 | GPIO18 | GPIO22 | GPIO27 |
|----|----|----|----|
| A- | B- | A+ | B+ |
| 0 | 0 | 0 | 1 | 
| 0 | 0 | 1 | 0 | 
| 0 | 1 | 0 | 0 | 
| 1 | 0 | 0 | 0 | 


Half step mode (slighly quieter than full step mode)

| GPIO17 | GPIO18 | GPIO22 | GPIO27 |
|----|----|----|----|
| A- | B- | A+ | B+ |
| 0 | 0 | 0 | 1 | 
| 0 | 0 | 1 | 1 | 
| 0 | 0 | 1 | 0 | 
| 0 | 1 | 1 | 0 | 
| 0 | 1 | 0 | 0 | 
| 1 | 1 | 0 | 0 | 
| 1 | 0 | 0 | 0 | 
| 1 | 0 | 0 | 1 | 

To reverse the direction, just reverse the direction of iteration through the table

Wiring

- RED = Coil A+ 
- BLUE = Coil A- 
- WHITE = Coil B+
- YELLOW = Coil B-

Should a higher voltage be required for driving the stepper motor, it would be applied to pin 8 of L293D chip, instead of 5v.

![Wiring](/wiring-diagram.png)

Usage
In one terminal window, start the service on default port 5000: 
```
python3 ./StarTracker.py
```

In a second terminal type one of commands without curly braces:
```
wget -o /dev/null http://127.0.0.1:5000/{start|stop|pause|resume|faster|slower|reverse}
```

Alternatively connect to a web browser to URL:
```
http://0.0.0.0:5000/tracker
```

