# Given the following Y_true and Y_pred variables. 

# # Given values
# Y_true = [1,1,2,2,4]  # Y_true = Y (original values)
  
# # calculated values
# Y_pred = [0.8,1.27,1.80,2.79,3.5]  # Y_pred = Y'

# Create a function that can calculate mean square error (MSE)! 
#   \begin{equation*}  MSE = \frac{1}{N}\sum_{i=1}^{N}(Y_i - \hat{Y}_i)^2  \end{equation*} 


Y_true = [1,1,2,2,4]
Y_pred = [0.8,1.27,1.80,2.79,3.5]
jumlah = 0 
n = len(Y_true) 
for i in range (0,n):  
  difference = Y_true[i] - Y_pred[i]  
  y = difference**2  
  jumlah = jumlah + y  
mse = jumlah/n  
print("Mean Square Error-nya adalah " , mse)