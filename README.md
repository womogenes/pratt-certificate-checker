# Pratt certificate verification

It's simple to verify with a computer that a number is probably prime. There exist primality tests that are very very good, such as the [Miller-Rabin primality test](https://youtu.be/zmhUlVck3J0), and they can determine with very high probability that a given number is prime.

However, it's much harder to for certain _prove_ that a number is prime. It is possible to prove that a number $n$ is prime if we provide the prime factorization of $n - 1$ with something called a [Pratt certificate](https://en.wikipedia.org/wiki/Primality_certificate#Pratt_certificates). This is an implementation of the algorithm for checking a Pratt certificate.

- Inside `pratt-certificate-verifier.py` there's a function called `pratt_verifier` that takes in a Pratt certificate and throws an error if something goes wrong.
- Inside `example_cert.py` there's an example certificate for the prime `111111111111111111131111111111111111111`.
