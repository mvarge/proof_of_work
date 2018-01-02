# Proof-of-Work experiment
Simple Proof-of-Work experiment in Python

## About
This program is an experiment to better understand how a proof-of-work algorithm works similar to the ones used for BitCoin, mailing, DoS, etc systems use. It reads a prototype string and calculates the SHA256 hash probabilities based on the required level of success (aka leading zeroes).

## References
The guidelines were based on the [Proof-of-Work](https://en.bitcoin.it/wiki/Proof_of_work) documentation available on bitcoing wiki.

## Examples

```
$ ./proof_of_work.py -s "test_string" -l 1 -v
Try: 1 - 86f21b3a88bc5e6c8254008ce9cc1330fa2256c6c2f07164e32c596bc9290838
Try: 2 - 72964de779ec3d3a7bed536084e9caa09b98b58590f9eba70503835e2451fa1c
Try: 3 - 2d21f5427b0889a5b0b08ae41d0d43679985c7cfbe6014f39842fef2d14c0a64
Try: 4 - 726ba2310823d5adcbff48e0dd83912fcd291c371c4fe08dd570773e965a5888
Try: 5 - caeb9c79c772fc4ecc0f33ec042951d0287bd2df636fc97e78543fe38ab3bedf
Try: 6 - ea129232d19603bf5df5d483b10b513a6b6bb7ad9dab1590eadeed385ec8dc2b
Try: 7 - f3dc044ec191a443b4d229007cebc8a6d2d1a3254483408b09489b9910ae299e
Try: 8 - 2477535ac8d71c3ba0171e7bbecfb9b9676d2d958c22ad7cdcc9f29c53311e9c
Try: 9 - 280f1acf1f44349c01fbb93613dcc1a1d0ac3b9e41b921978c00667e667e7607
Try: 10 - 9754134115c1f13be83903c9d1bd4866a7f50b0d9f54994978cded47905ba51e
Try: 11 - 74f0df9906a518ced1b66a782ee22f0eab47be7a8bdc9bd820c5e680cdc8f53b
Try: 12 - 0401c5638f37aaa7cae6676dfa32d1470142add690c50430edadd3052714ab2c
Coin costed 12 tests.
```

```
$ ./proof_of_work.py -s "test_string" --level=4
Coin costed 186613 tests.
```

## Author

Marcelo Marques da Silva Varge
(marcelo.varge@gmail.com)
