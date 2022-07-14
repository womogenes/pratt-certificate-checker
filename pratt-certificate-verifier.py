def pratt_verifier(cert):
    """
    Verifies that a Pratt certificate is correct.
    cert is a dictionary where:
        - keys are primes n
        - values are a list:
            [0] Witness (int)
            [1] List of tuples (p, e) as a factorization
                of n - 1. Alternatively, just the integer
                p may be provided if e=1.
    """
    # Verify each prime in the certificate
    for n in cert:
        if n == 2:
            # Yes, 2 is automatically prime
            continue

        a = cert[n][0]
        factorization = cert[n][1]

        # Confirm the factorization holds up
        prod = 1
        for part in factorization:
            if isinstance(part, int):
                p, e = part, 1
            else:
                p, e = part
            if p != 2 and not p in cert:
                raise ValueError(
                    f"{p} is not certified as a prime in the factorization of {n} - 1.")
            prod = (prod * pow(p, e, n - 1)) % (n - 1)

        if prod != 0:
            raise ValueError(f"The factorization for {n} - 1 is invalid.")

        # Perform a^(n-1) check
        if pow(a, n - 1, n) != 1:
            raise ValueError(f"a^(n-1) check failed for n={n}.")

        # Perform smaller order check
        for part in factorization:
            q = part if isinstance(part, int) else part[0]
            if pow(a, (n - 1) // q, n) == 1:
                raise ValueError(f"a^((n-1)/q) check failed for {n}.")

        print(f"Checks passed for n={n}.")

    return True


if __name__ == "__main__":
    from example_cert import CERT
    print(pratt_verifier(CERT))
