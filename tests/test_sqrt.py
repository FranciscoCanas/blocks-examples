import tempfile

from blocks.extensions.saveload import SAVED_TO

from sqrt import main


def test_sqrt():
    save_path = tempfile.mkdtemp()
    main(save_path, 7)
    main_loop = main(save_path, 14, continue_=True)
    assert main_loop.log[7][SAVED_TO] == save_path
