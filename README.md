# Containers

This is a greedy algorithm implementation on Python for my college.

## How it works

This algorithm is pretty simple, it generates a random list of items. Each item's value from the list is divided by its weight to get its value per weight, the list is later sorted by this value.

After we get this sorted list fill the container is just really easy, we just look the container capacity and if the item can do it inside of it. If the item can't then a percentage is calculated to know how much of the item can. Then this percentage is stored on the container and the process is repeated until it's full.

## Tests

To execute the tests in a easy way ```pytest``` can be used.

## Requirements

None

## How to use

Just as any Python module, execute the ```main.py``` file with Python and specify a quantity of items to generate.
