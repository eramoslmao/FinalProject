# FinalProject
#Simple Cost Estimation Program
---
This program calculates the costs for
specific materials and labor specifications for a project of a certain length

Assumptions:
* max cost of labor by assuming pay throughout the project time frame
* labor specified will stay throughout the entirety of the project
* amount of materials in tons or area is already known
* installation prices are preset by the program

Inputs:
* area needed of concrete
* planks of wood
* tons of steel
* project time frame
* type of wood
* type of steel material
* type of labor

Outputs:
* subtotal cost of each material
* cost of installation for each material
* cost for labor throughout the project

## Setup
To use this program, this repository should be cloned/downloaded. Make sure you have Python 3.0 installed.

## How to use the program
When running the program will display the material dictionaries and labor dictionary
First enter how long the project will last for.\
`How long is your project (in weeks?): 15`\
Next you will be asked to input how much area needs to be covered.\
`How much area needs to be covered? (in sq ft): 50`\
Next input the amount of planks needed for the wood material.\
`How many planks of wood are needed?: 15`\
Next choose the wood material from the displayed dictionary.\
`What kind of wood do you need? Choose from our selection: plywood`\
Then specify the amount of steel needed per ton.\
`How much steel is needed? (per ton) 50`\
Next choose the steel item from the displayed dictionary.\
`What kind of steel do you need? Choose from our selection: w14 beam`\
Afterwards choose the labor type from the displayed dictionary.\
`What kind of labor do you need? Choose from our selection: electrician`\
Any misspelling or non existent material choice will result in an error. It is optimal to input in all lowercase, exactly as the dictionary displays

Given those inputs the program should output the calculated costs for each material, along with installation and total costs for each. Labor should also be calculated.

## How to use the program

Given the material and how much is needed per unit, the cost of each material should be calculated.

First instantiate a new object of ``Project``:

```python
>>> main = WorkEstimate('Project')
```
The project will ask you for the inputs and then the results may be displayed
```python
>>> print(main.output())
```
