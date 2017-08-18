# Star Tracker

Control of a stepepr motor for a "Barn Door Tracker"

## Sequence on GPIO ports

Full step

| GPIO17 | GPIO18 | GPIO22 | GPIO27 |
|----|----|----|----|
| 0 | 0 | 0 | 1 | 
| 0 | 0 | 1 | 0 | 
| 0 | 1 | 0 | 0 | 
| 1 | 0 | 0 | 0 | 


Half step

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

To reverse the direction just, reverse the direction of iteration through the table

Wiring
![Wiring](/wiring-diagram.png)
