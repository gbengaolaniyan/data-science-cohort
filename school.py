# Just an example for data science course
def rank(data):
    sorted_data = sorted(data)
    ranks=[]
    for value in data:
        first=sorted_data.index(value)+1
        count=sorted_data.count(value)
        ranks.append(first+(count-1)/2)
    return ranks

def spearman(x,y):
    n=len(y)
    rx,ry=rank(x),rank(y)
    d_squared=sum((a-b)**2 for a,b in zip(rx,ry))
    return 1-(6*d_squared)/(n*(n**2-1))
x=[86,97,99,100,101,103,106,110,112,113,98]
y=[2,6,7,12,17,20,27,28,29,50,40]
print(f"Spearman rho = {spearman(x,y):.4f}")