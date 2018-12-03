def strip_list(l):
    return map(lambda s: s.strip(), l)

def to_ints(l):
    return map(int, l)

class FabricLayout(object):

    def claim_squares(self, claim, include_claim_id=False):
        claim_id, more = strip_list(claim.split("@"))
        offsets, dims = strip_list(more.split(":"))
        x_offset, y_offset = map(int, offsets.split(","))
        x_dim, y_dim = map(int, dims.split("x"))

        for x in range(x_offset, x_offset + x_dim):
            for y in range(y_offset, y_offset + y_dim):
                yield include_claim_id and (claim_id, x, y) or (x, y)

    def overlapping_inches(self, input_):
        one_claimed_squares = set()
        multi_claimed_squares = set()
        for claim_def in input_:
            for claim in self.claim_squares(claim_def):
                if claim in multi_claimed_squares:
                    continue

                if claim in one_claimed_squares:
                    multi_claimed_squares.add(claim)
                else:
                    one_claimed_squares.add(claim)

        return multi_claimed_squares

    def disjoint_claim(self, input_):
        overlapping_inches = self.overlapping_inches(input_)
        for claim_def in input_:
            overlapping_claim_or_none = None
            for id_, x, y in self.claim_squares(claim_def, include_claim_id=True):
                if (x, y) in overlapping_inches:
                    overlapping_claim_or_none = id_
                    break

            if overlapping_claim_or_none is not None:
                continue

            return id_.strip("#")


def challenge1():
    with open("inputs/fabric-claims.txt", "r") as fd:
        bc = FabricLayout()
        return len(bc.overlapping_inches(fd.readlines()))


def challenge2():
    with open("inputs/fabric-claims.txt", "r") as fd:
        bc = FabricLayout()
        # 1019
        return bc.disjoint_claim(fd.readlines())


if __name__ == "__main__":
    print(challenge2())
