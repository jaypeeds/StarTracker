# Star Tracker

Control of a stepepr motor for a "Barn Door Tracker"

## Sequence on GPIO ports

Full step mode

| GPIO17 | GPIO18 | GPIO22 | GPIO27 |
|----|----|----|----|
| 0 | 0 | 0 | 1 | 
| 0 | 0 | 1 | 0 | 
| 0 | 1 | 0 | 0 | 
| 1 | 0 | 0 | 0 | 


Half step mode (slighly quieter than full step mode)

| GPIO17 | GPIO18 | GPIO22 | GPIO27 |
|----|----|----|----|
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

- RED = Coil A start
- BLUE = Coil A end
- WHITE = Coil B start
- YELLOW = Coil B end

Should a higher voltage be required for driving the stepper motor, it would be applied to pin 8 of L293D chip, instead of 5v.

![Wiring](/wiring-diagram.png)
