# 106bombyx

Chaos theory analysis and the logistic map.

Project for semester 2 of the Epitech Math module.

### Description

This project studies the evolution of populations using a growth model. The program computes and outputs data, as a bonus a graph is created using `matplotlib`.

1. The population curve over 100 generations.
2. A synthetic scheme showing population values depending on growth rate (k).

## Getting Started

### Dependencies

- [Python3](https://python.org/)

### Installation

* Download/Clone the repository and enter its directory.
* Run `pip3 install -r requirements.txt` to install the necesary libraries
* Now you are ready to run the code.

## Usage

**Execution:** `./106bombyx n [k | i0 i1]`

### Arguments
- **`n`**: Number of first-generation individuals.
- **`k`**: Growth rate (1 to 4).
- **`i0`**, **`i1`**: Initial and final generation.

### Examples

To output data for 10 generations with growth rate 3.3:
```
$> ./106bombyx 10 3.3
```

To plot population values between 10000 and 10010 generations:
```
$> ./106bombyx 10 10000 10010
```

## Acknowledgments

* [Epitech](https://www.epitech.eu/)

## Authors

* **Daniel Sanchez** ([GitHub](https://github.com/angsanch) / [LinkedIn](https://www.linkedin.com/in/angeldanielsanchez/))
* **Xinru Xu** ([GitHub](https://github.com/Exinru) / [LinkedIn](https://www.linkedin.com/in/xinru-xu/))

## License

This project is licensed under the GNU Public License version 3.0 - see the [LICENSE](LICENSE) file for details.
