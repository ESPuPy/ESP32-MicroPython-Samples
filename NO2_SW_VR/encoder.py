#-----------------------------------------
#list4 encoder.py
#-----------------------------------------
#
# this program is designed for  Alps Alpine EC12E2420801 
# https://docs.rs-online.com/1497/0900766b80f4c3d5.pdf
#

class RotaryEncoder():

    def __init__(self,sig_A,sig_B):

        self.sig_A = sig_A 
        self.sig_B = sig_B
        self.last_val = None
        self.rotate_dir = None  # dir:'CW' or 'CCW'
        self.dbg_mode = False

    def get_val(self):

        enc_data = None
    
        val_A = self.sig_A.value()
        val_B = self.sig_B.value()
        val = val_A << 1 | val_B

        if self.dbg_mode:
            print(val,end="")

        if val == self.last_val:
            pass

        else:
            if self.last_val == 3:
                if val == 1:
                    self.rotate_dir = 'CW'
                elif val == 2:
                    self.rotate_dir = 'CCW'
                else:
                    pass

            elif val == 3:
                if self.rotate_dir == 'CW' and self.last_val == 2:
                    enc_data = 1
                    self.rotate_dir = None
                elif self.rotate_dir == 'CCW' and self.last_val == 1:
                    enc_data = -1
                    self.rotate_dir = None
                else:
                    enc_data = None
                    self.rotate_dir = None
            else:
                pass     # should be checked the transaction, but omitting...

            self.last_val = val
    
        return enc_data
    
    def set_dbg_mode(self, mode):

        self.dbg_mode = mode
