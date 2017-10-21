import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  scores = (np.dot(X, W))
  num_train = X.shape[0]
  for i in xrange(num_train):
    scores[i] -= np.max(scores[i])
    scores[i] = np.exp(scores[i])
    summer = np.sum(scores[i])
    scores[i] /= summer
    loss += -np.log(scores[i, y[i]])
    
  dscores = scores
  dscores[range(num_train), y] -= 1
  dscores /= num_train
  
  dW = np.dot(X.T, dscores)
  dW += reg*W
  loss /= num_train
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  scores = np.dot(X, W)
  num_train = X.shape[0]
  scores -= np.max(scores, axis=1, keepdims=True)
  scores = np.exp(scores)
  summer = np.sum(scores, axis=1)
  summer = summer[:, np.newaxis]
  scores /= summer
  
  loss = np.sum(-np.log(scores[range(num_train), y]))
  loss /= num_train
    
  dscores = scores
  dscores[range(num_train), y] -= 1
  dscores /= num_train
  dW = np.dot(X.T, dscores)
  dW +=reg*W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

