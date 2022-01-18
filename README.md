# Coding Task 2 

Implements the function merge, which receives a list of intervals and merges them if they overlap.

## Setup 

Requirements:
- python 3.8
- [memory-profiler](https://pypi.org/project/memory-profiler/)

```
git clone https://github.com/Goldyy/CodingTask2.git
cd CodingTask2/
```

If you have conda, create a conda env with the required modules:
```
conda create -n <env> python=3.8
conda activate <env>
pip install -r requirements.txt
```
Or use **setup_conda.sh** and activate the conda env called "interval_merge" to execute the program and tests.

If you want to use virtualenv:
```
pip install virtualenv
virtualenv <env>
source <env>/bin/activate
pip install -r requirements.txt
```

## Execution

Start the program with the example input:
```
python main.py
```
Or use custom intervals:
```
python main.py -i 25 30 -i 2 19 -i 14 23 -i 4 8
```


## Tests

Run the tests with:
```
python -m unittest tests/test_merge.py
```

## Questions

#### Wie ist die Laufzeit Ihres Programms?
> Eingabe: [[25,30], [2,19], [14, 23], [4,8]]
> 
> Die Laufzeit beträgt ~28 µs
> 
> Sortieren: sorted() -> O(n log n), Mergen -> O(n) 

#### Wie kann die Robustheit sichergestellt werden, vor allem auch mit Hinblick auf sehr große Eingaben?

>  Es könnte ein Type-checking in der Funktion eingebaut werden (Liste einer Liste von Integers) oder nach der korrekten Angabe von Intervallgrenzen überprüft werden ([min, max]).
>
#### Wie verhält sich der Speicherverbrauch ihres Programms?
> Eingabe: [[25,30], [2,19], [14, 23], [4,8]]
>
> Der Speicherverbrauch beträgt 36.9 MiB
>
> Eingabe: [[x, x + 2] for x in range(0, 1000000, 4)] (250.000 Intervalle)
>
> Der Speicherverbrauch beträgt 90.2 MiB
>
> Für die zusammengefügten Intervalle wird zusätzlich maximal der Memory der Eingabeintervalle benötigt (O(n))