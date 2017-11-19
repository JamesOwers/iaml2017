import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

# Letter matrices - defined here so they are not carried by all objects
OMAT = np.array([[1,1,1],
                 [1,0,1],
                 [1,1,1]], dtype=int)
IMAT = np.array([[0,1,0],
                 [0,1,0],
                 [0,1,0]], dtype=int)
TMAT = np.array([[1,1,1],
                 [0,1,0],
                 [0,1,0]], dtype=int)
XMAT = np.array([[1,0,1],
                 [0,1,0],
                 [1,0,1]], dtype=int)
CMAT = np.array([[1,1,1],
                 [1,0,0],
                 [1,1,1]], dtype=int)


LETTERMATS = {
    'O': OMAT,
    'I': IMAT,
    'T': TMAT,
    'X': XMAT,
    'C': CMAT
}
LETTERMATS = {key: value.flatten() for (key, value) in LETTERMATS.iteritems()}

def load_letters(categories=['T', 'C'], num_obs=[5, 5], bounds=[-1, 1],
                 beta_params=None, shuffle=True, random_state=None):
    """Load a synthetic dataset of images containing letters. By default, pixel
    data is -1 or 1 for 'off' or 'on' respecively. Random noise can be added by
    supplying beta distribution parameters in the beta_params argument. The 
    bounds ([min, max] pixel values) can be changed by changing the bounds 
    argument (e.g. bounds=[0, 1] would make data between 0 and 1).
    
    Arguments
    ---------
    categories : list-like, A collection of strings for the letters that should
        be included in the dataset. Must be in data.LETTERMATS.keys().
    num_obs : list, number of observations to generate for each category. 
        (Default [5, 5])
    beta_params: list, used for generating pixel data with noise
        list must be of form [[a_0, b_0], [a_1, b_1]] where a_n is the beta 
        parameter a for generating 0 pixels. Defualt None produces deterministic
        0 / 1 pixel data
    shuffle : Boolean, Whether to shuffle the rows of the data (Default True)
    random_state : int, random state to use for generation. Default, None uses
        current numpy random state
    
    Returns
    -------
    data : all data excluding the target
    target : numeric target classes to fit
    target_names : dict of category labels for numeric targets
    """
    assert all([cat in LETTERMATS for cat in categories]), \
        'Categories must be in the specified set [{}]'.format(LETTERMATS.keys())
    assert len(num_obs) == len(categories), 'Arguments "num_obs" and "categories" ' \
        'must be the same length'
    if random_state is not None:
        np.random.seed(random_state)
    num_dims = 9
    data = np.zeros((np.sum(num_obs), num_dims))
    target = np.zeros(np.sum(num_obs), dtype=int)
    target_names = dict(zip(range(len(categories)), categories))
    row_nr = 0
    cat_num_obs = dict(zip(categories, num_obs))
    for cat_id, cat in enumerate(categories):
        for ii in range(cat_num_obs[cat]):
            data[row_nr, :] = binary_beta_data(LETTERMATS[cat], beta_params=beta_params)
            target[row_nr] = cat_id
            row_nr += 1
    data_range = bounds[1] - bounds[0]
    data = data_range * data + bounds[0]
    if shuffle:
        idx = range(np.sum(num_obs))
        np.random.shuffle(idx)
        data = data[idx]
        target = target[idx]
    return data, target, target_names


def binary_beta_data(x, beta_params=None):
    """Takes as input binary data and returns noisy data sampled from a
    mixture of beta distributions.
    Arguments
    ---------
    x : array, array to add noise to
    beta_params: list, used for generating pixel data with noise
        list must be of form [[a_0, b_0], [a_1, b_1]] where a_n is the beta 
        parameter a for generating 0 pixels. Be careful with how you set these -
        you can easily 'flip' the data by setting the parameters the wrong way round.
        An example setting for a small amount of symmetrical noise would be
        [[1, 10], [10, 1]]. See: https://en.wikipedia.org/wiki/Beta_distribution
        (Defualt None produces deterministic data)
        0 / 1 pixel data
    """
    if beta_params is not None:
        assert len(beta_params) == 2, \
            'If setting beta_params, you must provide beta params for both on ' \
            'and off pixels, i.e. a list of form [[a_0, b_0], [a_1, b_1]]'
        x_noised = np.array([np.random.beta(*beta_params[pixel_val]) for pixel_val in x])
    else:
        x_noised = x
    return x_noised


# Classes ===
class Board:
    """
    Randomly generated 3-by-3 board configurations with equal probability for 
    black/white. The board is defined such that:
        -1 - missing (grey)
         0 - player0 (white)
         1 - player1 (black)
    This was done so we could extend and play larger games with more players 
    and the value for missing would stay the same.
    """
    board = np.zeros([9,], dtype=int) - 1  # init missing
    cmap = ListedColormap(['darkred', 'gray', 'white', 'black', 'red'])
    norm = BoundaryNorm([-np.inf, -1.5, -.5, .5, 1.5, np.inf], cmap.N)
    def __init__(self, populate=True):
        if populate:
            self.board = np.random.choice([0, 1], size=(9,))
    def show(self):
        plt.matshow(self.board.reshape([3, 3]), cmap=self.cmap, norm=self.norm)
    def invert(self):
        if -1 in self.board:
            missing = self.board == -1
            self.board = np.invert(self.board) + 2
            self.board[missing] = -1
        else:
            self.board = np.invert(self.board) + 2


class LetterBoard(Board):
    """A class to quickly print 3-by-3 board configurations"""
    def __init__(self, letter, populate=False):
        assert letter.lower() in LETTERMATS.keys(),\
            "{} is not an available letter".format(letter)
        self.board = LETTERMATS[letter.lower()]
        
