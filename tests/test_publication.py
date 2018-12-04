import os
import pytest

from kallysto.publication import Publication

def test_publication_is_a_publication(pub_with_defs):
    assert type(pub_with_defs) == Publication
    
def test_publication_data_store(pub_with_defs): 
    """Check for the main data store directories and files."""
    
    # Check the title directory exists
    assert os.path.isdir(pub_with_defs.pub_path) is True
    
    # Check each of the main data store dirs exist.
    for name in ['data', 'figs', 'defs', 'logs']:
        dir_path = pub_with_defs.kallysto_path + getattr(pub_with_defs, '{}_path'.format(name))
        assert os.path.isdir(dir_path) is True
        
    # Check the src dir exists
    assert os.path.isdir(pub_with_defs.src_path) is True
        
    # Check the log file exists.
    logs_file = pub_with_defs.kallysto_path+pub_with_defs.logs_file
    assert os.path.isfile(logs_file) is True
    
def test_write_defs(pub_with_defs, pub_no_defs):
    """Test the write_defs behavior.
    
    Make sure that a _definitions.tex is created when write_defs
    is True and that there is no file created when write_defs is False."""
    
    assert pub_with_defs.write_defs is True
    
    with_defs_file = pub_with_defs.kallysto_path+pub_with_defs.defs_file
    
    assert os.path.isfile(with_defs_file) is True


    assert pub_no_defs.write_defs is False
    
    no_defs_file = pub_no_defs.kallysto_path+pub_no_defs.defs_file
    assert os.path.isfile(no_defs_file) is False
    

    
def test_markdown_publication_data_store(pub_using_markdown): 
    """Check for the main data store directories and files."""
    
    # Check the title directory exists
    assert os.path.isdir(pub_using_markdown.pub_path) is True
    
    # Check each of the main data store dirs exist.
    for name in ['data', 'figs', 'defs', 'logs']:
        dir_path = pub_using_markdown.kallysto_path + getattr(pub_using_markdown, '{}_path'.format(name))
        assert os.path.isdir(dir_path) is True
        
    # Check the src dir exists
    assert os.path.isdir(pub_using_markdown.src_path) is True
    
    # Check the log file exists.
    logs_file = pub_using_markdown.kallysto_path+pub_using_markdown.logs_file
    assert os.path.isfile(logs_file) is True