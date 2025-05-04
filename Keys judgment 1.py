    
def can_dissociate(sequence):
    """Determine if sequence can dissociate (contains 'X')"""
    return 'X' in ''.join(sequence.split())

def get_complementary(seq):
    """Generate complementary sequence with 5' to 3' direction"""
    base_pairing = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([base_pairing.get(base, base) for base in reversed(seq)])

def check_match(lk_seq, rk_seq, window_size=10):
    """Check for 10 complementary base pairs between sequences"""
    lk_clean = lk_seq.replace('X', '')
    if len(lk_clean) < window_size:
        return False
    lk_windows = {lk_clean[i:i+window_size] for i in range(len(lk_clean) - window_size + 1)}

    rk_clean = rk_seq.replace('X', '')
    rk_complementary = get_complementary(rk_clean)
    if len(rk_complementary) < window_size:
        return False

    for i in range(len(rk_complementary) - window_size + 1):
        rk_window = rk_complementary[i:i+window_size]
        if rk_window in lk_windows:
            return True
    return False


def process_groups(lk_groups, rk_groups):
    dissociable_lk = []
    for lk_idx, lk_seq in enumerate(lk_groups, 1):
        lk_combined = ''.join(lk_seq.split())
        if can_dissociate(lk_combined):
            dissociable_lk.append((lk_idx, lk_combined))
        else:
            print(f"Lk{lk_idx} -×")

    for lk_idx, lk_combined in dissociable_lk:
        for rk_idx, rk_seq in enumerate(rk_groups, 1):
            rk_combined = ''.join(rk_seq.split())
            if check_match(lk_combined, rk_combined):
                print(f"Lk{lk_idx} -> Rk{rk_idx}")
            else:
                print(f"Lk{lk_idx} -×- Rk{rk_idx}")


original_lk_groups = [Lk1, Lk2, Lk3]
new_rk_groups = [Rk1, Rk2, Rk3 ]

process_groups(original_lk_groups, new_rk_groups)
    
