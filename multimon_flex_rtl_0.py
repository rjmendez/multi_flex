#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Multimon Flex Rtl 0
# Generated: Tue Oct 10 19:26:54 2017
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import time


class multimon_flex_rtl_0(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Multimon Flex Rtl 0")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2.4e6
        self.channel_1 = channel_1 = 929.65e6
        self.channel_0 = channel_0 = 929.6e6
        self.xlate_filter_taps = xlate_filter_taps = firdes.low_pass(1, samp_rate, 125000, 25000, firdes.WIN_HAMMING, 6.76)
        self.sqlch = sqlch = -50
        self.if_gain = if_gain = -14
        self.gain = gain = 50
        self.firdes_tap = firdes_tap = firdes.low_pass(1, samp_rate, 125000, 25000, firdes.WIN_HAMMING, 6.76)
        self.corr = corr = -14
        self.center_freq_0 = center_freq_0 = sum([channel_0, channel_1] ) / float(len([channel_0, channel_1]))
        self.bb_gain = bb_gain = 40

        ##################################################
        # Blocks
        ##################################################
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + 'rtl=0' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(center_freq_0 - 100000, 0)
        self.osmosdr_source_0.set_freq_corr(corr, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(2, 0)
        self.osmosdr_source_0.set_gain_mode(True, 0)
        self.osmosdr_source_0.set_gain(gain, 0)
        self.osmosdr_source_0.set_if_gain(if_gain, 0)
        self.osmosdr_source_0.set_bb_gain(bb_gain, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, 48e3, 6.5e3, 2e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, 48e3, 6.5e3, 2e3, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fir_filter_xxx_0_0 = filter.freq_xlating_fir_filter_ccc(int(samp_rate / 48000), (firdes_tap), channel_1 - center_freq_0, samp_rate)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(int(samp_rate / 48000), (firdes_tap), channel_0 - center_freq_0, samp_rate)
        self.blocks_udp_sink_1 = blocks.udp_sink(gr.sizeof_short*1, '127.0.0.1', 7301, 1472, True)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_short*1, '127.0.0.1', 7300, 1472, True)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_2 = blocks.multiply_const_vff((0.1, ))
        self.blocks_multiply_const_vxx_0_0_1 = blocks.multiply_const_vff((0.1, ))
        self.blocks_float_to_short_0_1 = blocks.float_to_short(1, 32767)
        self.blocks_float_to_short_0_0 = blocks.float_to_short(1, 32767)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -100000, 1, 0)
        self.analog_pwr_squelch_xx_0_2 = analog.pwr_squelch_cc(sqlch, 1, 1, True)
        self.analog_pwr_squelch_xx_0_0_1 = analog.pwr_squelch_cc(sqlch, 1, 1, True)
        self.analog_nbfm_rx_0_0 = analog.nbfm_rx(
        	audio_rate=48000,
        	quad_rate=48000,
        	tau=75e-6,
        	max_dev=5000,
          )
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=48000,
        	quad_rate=48000,
        	tau=75e-6,
        	max_dev=5000,
          )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_rx_0, 0), (self.blocks_multiply_const_vxx_0_2, 0))
        self.connect((self.analog_nbfm_rx_0_0, 0), (self.blocks_multiply_const_vxx_0_0_1, 0))
        self.connect((self.analog_pwr_squelch_xx_0_0_1, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.analog_pwr_squelch_xx_0_2, 0), (self.low_pass_filter_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_float_to_short_0_0, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.blocks_float_to_short_0_1, 0), (self.blocks_udp_sink_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_1, 0), (self.blocks_float_to_short_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_2, 0), (self.blocks_float_to_short_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.freq_xlating_fir_filter_xxx_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_pwr_squelch_xx_0_2, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.analog_pwr_squelch_xx_0_0_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_nbfm_rx_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.analog_nbfm_rx_0_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_firdes_tap(firdes.low_pass(1, self.samp_rate, 125000, 25000, firdes.WIN_HAMMING, 6.76))
        self.set_xlate_filter_taps(firdes.low_pass(1, self.samp_rate, 125000, 25000, firdes.WIN_HAMMING, 6.76))
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_channel_1(self):
        return self.channel_1

    def set_channel_1(self, channel_1):
        self.channel_1 = channel_1
        self.set_center_freq_0(sum([self.channel_0, self.channel_1] ) / float(len([self.channel_0, self.channel_1])))
        self.freq_xlating_fir_filter_xxx_0_0.set_center_freq(self.channel_1 - self.center_freq_0)

    def get_channel_0(self):
        return self.channel_0

    def set_channel_0(self, channel_0):
        self.channel_0 = channel_0
        self.set_center_freq_0(sum([self.channel_0, self.channel_1] ) / float(len([self.channel_0, self.channel_1])))
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.channel_0 - self.center_freq_0)

    def get_xlate_filter_taps(self):
        return self.xlate_filter_taps

    def set_xlate_filter_taps(self, xlate_filter_taps):
        self.xlate_filter_taps = xlate_filter_taps

    def get_sqlch(self):
        return self.sqlch

    def set_sqlch(self, sqlch):
        self.sqlch = sqlch
        self.analog_pwr_squelch_xx_0_2.set_threshold(self.sqlch)
        self.analog_pwr_squelch_xx_0_0_1.set_threshold(self.sqlch)

    def get_if_gain(self):
        return self.if_gain

    def set_if_gain(self, if_gain):
        self.if_gain = if_gain
        self.osmosdr_source_0.set_if_gain(self.if_gain, 0)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.osmosdr_source_0.set_gain(self.gain, 0)

    def get_firdes_tap(self):
        return self.firdes_tap

    def set_firdes_tap(self, firdes_tap):
        self.firdes_tap = firdes_tap
        self.freq_xlating_fir_filter_xxx_0_0.set_taps((self.firdes_tap))
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.firdes_tap))

    def get_corr(self):
        return self.corr

    def set_corr(self, corr):
        self.corr = corr
        self.osmosdr_source_0.set_freq_corr(self.corr, 0)

    def get_center_freq_0(self):
        return self.center_freq_0

    def set_center_freq_0(self, center_freq_0):
        self.center_freq_0 = center_freq_0
        self.osmosdr_source_0.set_center_freq(self.center_freq_0 - 100000, 0)
        self.freq_xlating_fir_filter_xxx_0_0.set_center_freq(self.channel_1 - self.center_freq_0)
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.channel_0 - self.center_freq_0)

    def get_bb_gain(self):
        return self.bb_gain

    def set_bb_gain(self, bb_gain):
        self.bb_gain = bb_gain
        self.osmosdr_source_0.set_bb_gain(self.bb_gain, 0)


def main(top_block_cls=multimon_flex_rtl_0, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
