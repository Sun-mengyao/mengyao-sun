def can_dissociate(sequence):
    return 'X' in sequence


def get_complementary(seq):
    base_pairing = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([base_pairing.get(base, base) for base in reversed(seq)])


def check_match(lk_seq, pk_seq, window_size=10):
    lk_clean = lk_seq.replace('X', '')
    lk_windows = {lk_clean[i:i + window_size] for i in range(len(lk_clean) - window_size + 1)}

    pk_clean = pk_seq.replace('X', '')
    complementary_pk = get_complementary(pk_clean)

    for i in range(len(complementary_pk) - window_size + 1):
        if complementary_pk[i:i + window_size] in lk_windows:
            return True
    return False



def process_sequences(lk_groups, pk_groups, ck_groups):

    pk_lk_matches = {}
    for lk_idx, lk in enumerate(lk_groups, 1):
        lk_combined = ''.join(lk.split())
        if can_dissociate(lk_combined):
            for pk_idx, pk in enumerate(pk_groups, 1):
                pk_combined = ''.join(pk.split())
                if check_match(lk_combined, pk_combined):
                    pk_lk_matches[pk_idx] = lk_idx
                    print(f"Lk{lk_idx} -> Pk{pk_idx}")
                else:
                    print(f"Lk{lk_idx} -×- Pk{pk_idx}")
        else:
            for pk_idx in range(1, len(pk_groups) + 1):
                print(f"Lk{lk_idx} cannot dissociate - Lk{lk_idx} -×- Pk{pk_idx}")


    for ck_idx, ck in enumerate(ck_groups, 1):
        if ck_idx in pk_lk_matches:
            lk_idx = pk_lk_matches[ck_idx]
            lk = lk_groups[lk_idx - 1]
            lk_combined = ''.join(lk.split())
            ck_combined = ''.join(ck.split())
            if check_match(lk_combined, ck_combined):
                print(f"Lk{lk_idx} -> Ck{ck_idx}")
            else:
                print(f"Lk{lk_idx} -×- Ck{ck_idx}")
        else:
            print(f"No matched Lk for Ck{ck_idx} - skipped")



Lk_groups = [Lk1, Lk2, Lk3]

Pk_groups = [Pk1, Pk2, Pk3]

Ck_groups = [Ck1, Ck2, Ck3]

process_sequences(Lk_groups, Pk_groups, Ck_groups)
    
    
    
