import sys, os
import StringIO
import tempfile
import numpy as np
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)

import unittest
from oommftools import oommfdecode


import StringIO
from oommftools.fnameutil import filterOnExtensions


class Test_oommfdecode_text(unittest.TestCase):
    def setUp(self):
        self.test_files_folder = 'testfiles'
        self.vector_file_text = os.path.join(TEST_DIR, 
                                        self.test_files_folder,
                                        'dw_edgefield_cut_cell4_160.ohf')
        self.headers_test = {'ystepsize': 4e-09, 'xnodes': 1250.0, 'valuemultiplier': 258967.81743932367, 'xbase': 2e-09, 'zstepsize': 8e-09, 'znodes': 1.0, 'zbase': 4e-09, 'ynodes': 40.0, 'ybase': 2e-09, 'xstepsize': 4e-09}
        self.extraCaptures_test =  {'MIFSource': 'C:/programs/oommf_old/simus/DW-150-8-transverse/DW_edgefield/dw_edgefield.mif', 'Iteration': 0.0, 'SimTime': 0.0, 'Stage': 0.0}
        self.vector_file_binary = os.path.join(TEST_DIR, 
                                        self.test_files_folder,
                                        'h2h_leftedge_40x4.ohf')

        self.targetarray_pickle = os.path.join(TEST_DIR, 
                                        self.test_files_folder,
                                        'targetarray_text.npy')
    def test_unpackFile_text_targetarray(self):
        (targetarray, headers, extraCaptures) = oommfdecode.unpackFile(self.vector_file_text)
        #np.save(self.targetarray_pickle, targetarray)
        self.assertEqual(targetarray.all(), np.load(self.targetarray_pickle).all())
        
    def test_unpackFile_text_headers(self):
        (targetarray, headers, extraCaptures) = oommfdecode.unpackFile(self.vector_file_text)
        self.assertEqual(headers, self.headers_test)
        
    def test_unpackFile_text_extracaptures(self):
        (targetarray, headers, extraCaptures) = oommfdecode.unpackFile(self.vector_file_text)
        self.assertEqual(extraCaptures, self.extraCaptures_test)

class Test_oommfdecode_binary(unittest.TestCase):
    def setUp(self):
        self.test_files_folder = 'testfiles'
        self.vector_file_binary = os.path.join(TEST_DIR, 
                                        self.test_files_folder,
                                        'h2h_leftedge_40x4.ohf')
        self.headers_test = {'ystepsize': 1e-08, 'xnodes': 160.0, 'valuemultiplier': 1.0, 'xbase': 5e-09, 'zstepsize': 1e-08, 'znodes': 4.0, 'zbase': 5e-09, 'ynodes': 40.0, 'ybase': 5e-09, 'xstepsize': 1e-08}
        
        self.extraCaptures_test =  {'MIFSource': '/local/home/donahue/oommf/app/oxs/examples/h2h_edgefield.mif', 'Iteration': 0.0, 'SimTime': 0.0, 'Stage': 0.0}
                                        
        self.targetarray_pickle = os.path.join(TEST_DIR, 
                                        self.test_files_folder,
                                        'targetarray_binary.npy')                                        
    def test_unpackFile_binary_targetarray(self):
        (targetarray, headers, extraCaptures) = oommfdecode.unpackFile(self.vector_file_binary)
        #np.save(self.targetarray_pickle, targetarray)
        self.assertEqual(targetarray.all(), np.load(self.targetarray_pickle).all())
        
    def test_unpackFile_binary_headers(self):
        (targetarray, headers, extraCaptures) = oommfdecode.unpackFile(self.vector_file_binary)
        self.assertEqual(headers, self.headers_test)
        
    def test_unpackFile_binary_extraCaptures(self):
        (targetarray, headers, extraCaptures) = oommfdecode.unpackFile(self.vector_file_binary)
        self.assertEqual(extraCaptures, self.extraCaptures_test)
        
class Test_pickleArray(unittest.TestCase):
    def setUp(self):
        self.array = np.array([1., 2., 3.]
        self.headers = {'Name': 'Headers', 'Value': 1}
        self.extraCaptures = {'Capture1': 1, 'Capture2': 'two'}
        self.filename = 'test'
        
    def test(self):
        oommftools.pickleArray(self.array, self.headers, self.extraCaptures, self.filename)
        
        
        
        
