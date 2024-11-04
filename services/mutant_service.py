class MutantService:
    def is_mutant(self, dna: list[str]) -> bool:
        sequences_found = 0
        for i in range(len(dna)):
            for j in range(len(dna[i])):
                if (self._has_horizontal_sequence(dna, i, j) or
                    self._has_vertical_sequence(dna, i, j) or
                    self._has_diagonal_sequence(dna, i, j)):
                    sequences_found += 1
                    if sequences_found > 1:
                        return True
        return False

    def _has_horizontal_sequence(self, dna, row, col):
        if col + 3 < len(dna[row]):
            return all(dna[row][col] == dna[row][col + k] for k in range(4))
        return False

    def _has_vertical_sequence(self, dna, row, col):
        if row + 3 < len(dna):
            return all(dna[row][col] == dna[row + k][col] for k in range(4))
        return False

    def _has_diagonal_sequence(self, dna, row, col):
        if row + 3 < len(dna) and col + 3 < len(dna[row]):
            return all(dna[row][col] == dna[row + k][col + k] for k in range(4))
        return False
