class Romberg:
    data = []

    def integrate(self, f: object, a: float=0, b: float=1, steps: int=5) -> int:
        h = b-a
        self.data = [[0 for _ in range(step)] for step in range(1, steps+2)]

        self.data[0][0] = 0.5*h * (f(a) + f(b))
        for i in range(1, steps+1):
            h /= 2
            integration = 0
            for j in range(1, 2**i, 2):
                integration += f(a + j*h)

            self.data[i][0] = 0.5*self.data[i-1][0] + h*integration
            for k in range(1, i+1):
                self.data[i][k] = self.data[i][k-1]
                self.data[i][k] += (self.data[i][k-1]-self.data[i-1][k-1])/(4**k-1)

        return self.data[steps][steps]

    def print_data(self, width: int=10, decimal: int=6):
        if self.data == []: return
        width = width+decimal if width < decimal else width
        max_row = len(self.data)
        max_col = len(self.data[-1])

        print("+-{:s}-+".format(5*"-"), end="")
        print("-{:s}-+".format(width*"-") * len(self.data[-1]))

        print("| {:^5s} |".format("n\k"), end="")
        for k in range(max_col):
            print(" {num:^{width}d} |".format(num=k, width=width), end="")
        print()
        
        print("+-{:s}-+".format(5*"-"), end="")
        print("-{:s}-+".format(width*"-") * len(self.data[-1]))

        for i in range(max_row):
            print("| {:^5d} |".format(i), end="")
            for j in range(max_col):
                if j <= i: 
                    print(" {num:{width}.{decimal}f} |".format(
                        num=self.data[i][j], width=width, decimal=decimal), end=""
                    )
                else: print(" {:s} |".format(width*" "), end="")
            print()
        
        print("+-{:s}-+".format(5*"-"), end="")
        print("-{:s}-+".format(width*"-") * len(self.data[-1]))

# Example of Usage
import math

if __name__ == "__main__":
    romberg = Romberg()
    f = lambda x: math.exp(x)

    I = romberg.integrate(f, a=0, b=1, steps=5)
    romberg.print_data(width=10, decimal=6)

    print(f"Integration result: {I}")
