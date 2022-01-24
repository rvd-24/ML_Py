import numpy as np
def gradientdescent(x,y):
    m_curr=b_curr=0
    iterations=10
    n=len(x)
    learning_rate=0.001

#The Mean Square Error function/Cost Function=(1/n)*Summation of((yi-(y))^2) where  y=mx+b The linear regression line
#So Cost function is = (1/n)*Summation of((yi-(mx+b))^2),Now differentiating wrt m and b we get md and bd,
#For Gradient Descent, first we need to set a learning rate by checking if cost is decreasing in order to get the global minima(this is the use of gradient descent, to reduce the cost function/optimize it)
#After setting the learning rate, we run the cost function a number of times(iterations).
        
    for i in range(iterations):
        y_predicted=m_curr*x+b_curr
        md=-(2/n)*sum(x*(y-y_predicted))
        bd=-(2/n)*sum(y-y_predicted)
        m_curr=m_curr-learning_rate*md
        b_curr=b_curr-learning_rate*bd
        cost=(1/n)*sum({val**2 for val in (y-y_predicted)})
        print("m {}, b {},iteration {},cost {}".format(m_curr,b_curr,i,cost))

x=np.array([1,2,3,4,5,])
y=np.array([5,7,9,11,13])
gradientdescent(x,y)