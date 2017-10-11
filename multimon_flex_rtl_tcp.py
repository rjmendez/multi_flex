#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Multimon Flex Rtl Tcp
# Generated: Mon Oct  9 23:44:44 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import osmosdr
import sys
import time
from gnuradio import qtgui


class multimon_flex_rtl_tcp(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Multimon Flex Rtl Tcp")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Multimon Flex Rtl Tcp")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "multimon_flex_rtl_tcp")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2.4e6
        self.channel_9 = channel_9 = 931.45e6
        self.channel_8 = channel_8 = 931.4e6
        self.channel_7 = channel_7 = 931.85e6
        self.channel_6 = channel_6 = 931.5e6
        self.channel_5 = channel_5 = 929.7e6
        self.channel_4 = channel_4 = 929.650e6
        self.channel_3 = channel_3 = 929.6e6
        self.channel_2 = channel_2 = 929.5e6
        self.channel_12 = channel_12 = 929.85e6
        self.channel_11 = channel_11 = 929.8e6
        self.channel_10 = channel_10 = 929.65e6
        self.channel_1 = channel_1 = 929.65e6
        self.channel_0 = channel_0 = 929.6e6
        self.xlate_filter_taps = xlate_filter_taps = firdes.low_pass(1, samp_rate, 125000, 25000, firdes.WIN_HAMMING, 6.76)
        self.variable_qtgui_range_0 = variable_qtgui_range_0 = 50
        self.sqlch = sqlch = -50
        self.if_gain = if_gain = 40
        self.gain = gain = 50
        self.firdes_tap = firdes_tap = firdes.low_pass(1, samp_rate, 125000, 25000, firdes.WIN_HAMMING, 6.76)
        self.corr = corr = -13.5
        self.channel_13 = channel_13 = 929.625e6
        self.center_freq_1 = center_freq_1 = sum([channel_6, channel_7] ) / float(len([channel_6, channel_7]))
        self.center_freq_0 = center_freq_0 = sum([channel_0, channel_1] ) / float(len([channel_0, channel_1]))
        self.center_freq = center_freq = sum([channel_0, channel_1, channel_2, channel_3, channel_4, channel_5, channel_6, channel_7, channel_8, channel_9, channel_10, channel_11, channel_12] ) / float(len([channel_0, channel_1, channel_2, channel_3, channel_4, channel_5, channel_6, channel_7, channel_8, channel_9, channel_10, channel_11, channel_12]))
        self.bb_gain = bb_gain = 40

        ##################################################
        # Blocks
        ##################################################
        self._sqlch_range = Range(-150, -20, 500, -50, 200)
        self._sqlch_win = RangeWidget(self._sqlch_range, self.set_sqlch, "sqlch", "counter_slider", float)
        self.top_layout.addWidget(self._sqlch_win)
        self._if_gain_range = Range(0, 60, 100, 40, 200)
        self._if_gain_win = RangeWidget(self._if_gain_range, self.set_if_gain, "if_gain", "counter", float)
        self.top_layout.addWidget(self._if_gain_win)
        self._gain_range = Range(0, 100, 100, 50, 200)
        self._gain_win = RangeWidget(self._gain_range, self.set_gain, "gain", "counter", float)
        self.top_layout.addWidget(self._gain_win)
        self._corr_range = Range(-100, 100, 100, -13.5, 200)
        self._corr_win = RangeWidget(self._corr_range, self.set_corr, "corr", "counter", float)
        self.top_layout.addWidget(self._corr_win)
        self._channel_7_tool_bar = Qt.QToolBar(self)
        self._channel_7_tool_bar.addWidget(Qt.QLabel("channel_7"+": "))
        self._channel_7_line_edit = Qt.QLineEdit(str(self.channel_7))
        self._channel_7_tool_bar.addWidget(self._channel_7_line_edit)
        self._channel_7_line_edit.returnPressed.connect(
        	lambda: self.set_channel_7(eng_notation.str_to_num(str(self._channel_7_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._channel_7_tool_bar)
        self._channel_6_tool_bar = Qt.QToolBar(self)
        self._channel_6_tool_bar.addWidget(Qt.QLabel("channel_6"+": "))
        self._channel_6_line_edit = Qt.QLineEdit(str(self.channel_6))
        self._channel_6_tool_bar.addWidget(self._channel_6_line_edit)
        self._channel_6_line_edit.returnPressed.connect(
        	lambda: self.set_channel_6(eng_notation.str_to_num(str(self._channel_6_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._channel_6_tool_bar)
        self._channel_1_tool_bar = Qt.QToolBar(self)
        self._channel_1_tool_bar.addWidget(Qt.QLabel("channel_1"+": "))
        self._channel_1_line_edit = Qt.QLineEdit(str(self.channel_1))
        self._channel_1_tool_bar.addWidget(self._channel_1_line_edit)
        self._channel_1_line_edit.returnPressed.connect(
        	lambda: self.set_channel_1(eng_notation.str_to_num(str(self._channel_1_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._channel_1_tool_bar)
        self._channel_0_tool_bar = Qt.QToolBar(self)
        self._channel_0_tool_bar.addWidget(Qt.QLabel("channel_0"+": "))
        self._channel_0_line_edit = Qt.QLineEdit(str(self.channel_0))
        self._channel_0_tool_bar.addWidget(self._channel_0_line_edit)
        self._channel_0_line_edit.returnPressed.connect(
        	lambda: self.set_channel_0(eng_notation.str_to_num(str(self._channel_0_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._channel_0_tool_bar)
        self._bb_gain_range = Range(0, 100, 100, 40, 200)
        self._bb_gain_win = RangeWidget(self._bb_gain_range, self.set_bb_gain, "bb_gain", "counter", float)
        self.top_layout.addWidget(self._bb_gain_win)
        self._variable_qtgui_range_0_range = Range(0, 100, 1, 50, 200)
        self._variable_qtgui_range_0_win = RangeWidget(self._variable_qtgui_range_0_range, self.set_variable_qtgui_range_0, "variable_qtgui_range_0", "counter_slider", float)
        self.top_layout.addWidget(self._variable_qtgui_range_0_win)
        self.osmosdr_source_0_0 = osmosdr.source( args="numchan=" + str(1) + " " + 'rtl=1' )
        self.osmosdr_source_0_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0_0.set_center_freq(center_freq_1 - 100000, 0)
        self.osmosdr_source_0_0.set_freq_corr(corr, 0)
        self.osmosdr_source_0_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0_0.set_iq_balance_mode(2, 0)
        self.osmosdr_source_0_0.set_gain_mode(True, 0)
        self.osmosdr_source_0_0.set_gain(gain, 0)
        self.osmosdr_source_0_0.set_if_gain(if_gain, 0)
        self.osmosdr_source_0_0.set_bb_gain(bb_gain, 0)
        self.osmosdr_source_0_0.set_antenna('', 0)
        self.osmosdr_source_0_0.set_bandwidth(0, 0)

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

        self.low_pass_filter_0_0_0_0_1 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, 48e3, 7.5e3, 5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0_0_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, 48e3, 7.5e3, 5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, 48e3, 7.5e3, 5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, 48e3, 7.5e3, 5e3, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fir_filter_xxx_0_0_0_0_1 = filter.freq_xlating_fir_filter_ccc(int(samp_rate / 48000), (firdes_tap), channel_6 - center_freq_1, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_0_0_0_0_0 = filter.freq_xlating_fir_filter_ccc(int(samp_rate / 48000), (firdes_tap), channel_7 - center_freq_1, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_0 = filter.freq_xlating_fir_filter_ccc(int(samp_rate / 48000), (firdes_tap), channel_1 - center_freq_0, samp_rate)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(int(samp_rate / 48000), (firdes_tap), channel_0 - center_freq_0, samp_rate)
        self._channel_9_tool_bar = Qt.QToolBar(self)
        self._channel_9_tool_bar.addWidget(Qt.QLabel("channel_9"+": "))
        self._channel_9_line_edit = Qt.QLineEdit(str(self.channel_9))
        self._channel_9_tool_bar.addWidget(self._channel_9_line_edit)
        self._channel_9_line_edit.returnPressed.connect(
        	lambda: self.set_channel_9(eng_notation.str_to_num(str(self._channel_9_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._channel_9_tool_bar)
        self._channel_8_tool_bar = Qt.QToolBar(self)
        self._channel_8_tool_bar.addWidget(Qt.QLabel("channel_8"+": "))
        self._channel_8_line_edit = Qt.QLineEdit(str(self.channel_8))
        self._channel_8_tool_bar.addWidget(self._channel_8_line_edit)
        self._channel_8_line_edit.returnPressed.connect(
        	lambda: self.set_channel_8(eng_notation.str_to_num(str(self._channel_8_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._channel_8_tool_bar)
        self._channel_5_tool_bar = Qt.QToolBar(self)
        self._channel_5_tool_bar.addWidget(Qt.QLabel("channel_5"+": "))
        self._channel_5_line_edit = Qt.QLineEdit(str(self.channel_5))
        self._channel_5_tool_bar.addWidget(self._channel_5_line_edit)
        self._channel_5_line_edit.returnPressed.connect(
        	lambda: self.set_channel_5(eng_notation.str_to_num(str(self._channel_5_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._channel_5_tool_bar)
        self._channel_4_tool_bar = Qt.QToolBar(self)
        self._channel_4_tool_bar.addWidget(Qt.QLabel("channel_4"+": "))
        self._channel_4_line_edit = Qt.QLineEdit(str(self.channel_4))
        self._channel_4_tool_bar.addWidget(self._channel_4_line_edit)
        self._channel_4_line_edit.returnPressed.connect(
        	lambda: self.set_channel_4(eng_notation.str_to_num(str(self._channel_4_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._channel_4_tool_bar)
        self._channel_3_tool_bar = Qt.QToolBar(self)
        self._channel_3_tool_bar.addWidget(Qt.QLabel("channel_3"+": "))
        self._channel_3_line_edit = Qt.QLineEdit(str(self.channel_3))
        self._channel_3_tool_bar.addWidget(self._channel_3_line_edit)
        self._channel_3_line_edit.returnPressed.connect(
        	lambda: self.set_channel_3(eng_notation.str_to_num(str(self._channel_3_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._channel_3_tool_bar)
        self._channel_2_tool_bar = Qt.QToolBar(self)
        self._channel_2_tool_bar.addWidget(Qt.QLabel("channel_2"+": "))
        self._channel_2_line_edit = Qt.QLineEdit(str(self.channel_2))
        self._channel_2_tool_bar.addWidget(self._channel_2_line_edit)
        self._channel_2_line_edit.returnPressed.connect(
        	lambda: self.set_channel_2(eng_notation.str_to_num(str(self._channel_2_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._channel_2_tool_bar)
        self._channel_13_tool_bar = Qt.QToolBar(self)
        self._channel_13_tool_bar.addWidget(Qt.QLabel("channel_13"+": "))
        self._channel_13_line_edit = Qt.QLineEdit(str(self.channel_13))
        self._channel_13_tool_bar.addWidget(self._channel_13_line_edit)
        self._channel_13_line_edit.returnPressed.connect(
        	lambda: self.set_channel_13(eng_notation.str_to_num(str(self._channel_13_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._channel_13_tool_bar)
        self._channel_12_tool_bar = Qt.QToolBar(self)
        self._channel_12_tool_bar.addWidget(Qt.QLabel("channel_12"+": "))
        self._channel_12_line_edit = Qt.QLineEdit(str(self.channel_12))
        self._channel_12_tool_bar.addWidget(self._channel_12_line_edit)
        self._channel_12_line_edit.returnPressed.connect(
        	lambda: self.set_channel_12(eng_notation.str_to_num(str(self._channel_12_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._channel_12_tool_bar)
        self._channel_11_tool_bar = Qt.QToolBar(self)
        self._channel_11_tool_bar.addWidget(Qt.QLabel("channel_11"+": "))
        self._channel_11_line_edit = Qt.QLineEdit(str(self.channel_11))
        self._channel_11_tool_bar.addWidget(self._channel_11_line_edit)
        self._channel_11_line_edit.returnPressed.connect(
        	lambda: self.set_channel_11(eng_notation.str_to_num(str(self._channel_11_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._channel_11_tool_bar)
        self._channel_10_tool_bar = Qt.QToolBar(self)
        self._channel_10_tool_bar.addWidget(Qt.QLabel("channel_10"+": "))
        self._channel_10_line_edit = Qt.QLineEdit(str(self.channel_10))
        self._channel_10_tool_bar.addWidget(self._channel_10_line_edit)
        self._channel_10_line_edit.returnPressed.connect(
        	lambda: self.set_channel_10(eng_notation.str_to_num(str(self._channel_10_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._channel_10_tool_bar)
        self.blocks_udp_sink_3_0_1 = blocks.udp_sink(gr.sizeof_short*1, '127.0.0.1', 7306, 1472, True)
        self.blocks_udp_sink_3_0_0_0 = blocks.udp_sink(gr.sizeof_short*1, '127.0.0.1', 7307, 1472, True)
        self.blocks_udp_sink_1 = blocks.udp_sink(gr.sizeof_short*1, '127.0.0.1', 7301, 1472, True)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_short*1, '127.0.0.1', 7300, 1472, True)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_2 = blocks.multiply_const_vff((0.1, ))
        self.blocks_multiply_const_vxx_0_0_1 = blocks.multiply_const_vff((0.1, ))
        self.blocks_multiply_const_vxx_0_0_0_0_0_1 = blocks.multiply_const_vff((0.1, ))
        self.blocks_multiply_const_vxx_0_0_0_0_0_0_0 = blocks.multiply_const_vff((0.1, ))
        self.blocks_float_to_short_0_1_0_0_1 = blocks.float_to_short(1, 32767)
        self.blocks_float_to_short_0_1_0_0_0_0 = blocks.float_to_short(1, 32767)
        self.blocks_float_to_short_0_1 = blocks.float_to_short(1, 32767)
        self.blocks_float_to_short_0_0 = blocks.float_to_short(1, 32767)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -100000, 1, 0)
        self.analog_pwr_squelch_xx_0_2 = analog.pwr_squelch_cc(sqlch, 1, 1, True)
        self.analog_pwr_squelch_xx_0_0_1 = analog.pwr_squelch_cc(sqlch, 1, 1, True)
        self.analog_pwr_squelch_xx_0_0_0_0_0_1 = analog.pwr_squelch_cc(sqlch, 1, 1, True)
        self.analog_pwr_squelch_xx_0_0_0_0_0_0_0 = analog.pwr_squelch_cc(sqlch, 1, 1, True)
        self.analog_nbfm_rx_0_0_0_0_1 = analog.nbfm_rx(
        	audio_rate=48000,
        	quad_rate=48000,
        	tau=75e-6,
        	max_dev=5000,
          )
        self.analog_nbfm_rx_0_0_0_0_0_0 = analog.nbfm_rx(
        	audio_rate=48000,
        	quad_rate=48000,
        	tau=75e-6,
        	max_dev=5000,
          )
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
        self.connect((self.analog_nbfm_rx_0_0_0_0_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0_0_0_0_0, 0))
        self.connect((self.analog_nbfm_rx_0_0_0_0_1, 0), (self.blocks_multiply_const_vxx_0_0_0_0_0_1, 0))
        self.connect((self.analog_pwr_squelch_xx_0_0_0_0_0_0_0, 0), (self.low_pass_filter_0_0_0_0_0_0, 0))
        self.connect((self.analog_pwr_squelch_xx_0_0_0_0_0_1, 0), (self.low_pass_filter_0_0_0_0_1, 0))
        self.connect((self.analog_pwr_squelch_xx_0_0_1, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.analog_pwr_squelch_xx_0_2, 0), (self.low_pass_filter_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.blocks_float_to_short_0_0, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.blocks_float_to_short_0_1, 0), (self.blocks_udp_sink_1, 0))
        self.connect((self.blocks_float_to_short_0_1_0_0_0_0, 0), (self.blocks_udp_sink_3_0_0_0, 0))
        self.connect((self.blocks_float_to_short_0_1_0_0_1, 0), (self.blocks_udp_sink_3_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0_0_0_0, 0), (self.blocks_float_to_short_0_1_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0_0_1, 0), (self.blocks_float_to_short_0_1_0_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_1, 0), (self.blocks_float_to_short_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_2, 0), (self.blocks_float_to_short_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.freq_xlating_fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.freq_xlating_fir_filter_xxx_0_0_0_0_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.freq_xlating_fir_filter_xxx_0_0_0_0_1, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_pwr_squelch_xx_0_2, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.analog_pwr_squelch_xx_0_0_1, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0_0_0_0_0, 0), (self.analog_pwr_squelch_xx_0_0_0_0_0_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0_0_0_1, 0), (self.analog_pwr_squelch_xx_0_0_0_0_0_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_nbfm_rx_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.analog_nbfm_rx_0_0, 0))
        self.connect((self.low_pass_filter_0_0_0_0_0_0, 0), (self.analog_nbfm_rx_0_0_0_0_0_0, 0))
        self.connect((self.low_pass_filter_0_0_0_0_1, 0), (self.analog_nbfm_rx_0_0_0_0_1, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.osmosdr_source_0_0, 0), (self.blocks_multiply_xx_0_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "multimon_flex_rtl_tcp")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_firdes_tap(firdes.low_pass(1, self.samp_rate, 125000, 25000, firdes.WIN_HAMMING, 6.76))
        self.set_xlate_filter_taps(firdes.low_pass(1, self.samp_rate, 125000, 25000, firdes.WIN_HAMMING, 6.76))
        self.osmosdr_source_0_0.set_sample_rate(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_channel_9(self):
        return self.channel_9

    def set_channel_9(self, channel_9):
        self.channel_9 = channel_9
        Qt.QMetaObject.invokeMethod(self._channel_9_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.channel_9)))
        self.set_center_freq(sum([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12] ) / float(len([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12])))

    def get_channel_8(self):
        return self.channel_8

    def set_channel_8(self, channel_8):
        self.channel_8 = channel_8
        Qt.QMetaObject.invokeMethod(self._channel_8_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.channel_8)))
        self.set_center_freq(sum([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12] ) / float(len([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12])))

    def get_channel_7(self):
        return self.channel_7

    def set_channel_7(self, channel_7):
        self.channel_7 = channel_7
        Qt.QMetaObject.invokeMethod(self._channel_7_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.channel_7)))
        self.set_center_freq_1(sum([self.channel_6, self.channel_7] ) / float(len([self.channel_6, self.channel_7])))
        self.freq_xlating_fir_filter_xxx_0_0_0_0_0_0.set_center_freq(self.channel_7 - self.center_freq_1)
        self.set_center_freq(sum([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12] ) / float(len([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12])))

    def get_channel_6(self):
        return self.channel_6

    def set_channel_6(self, channel_6):
        self.channel_6 = channel_6
        Qt.QMetaObject.invokeMethod(self._channel_6_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.channel_6)))
        self.set_center_freq_1(sum([self.channel_6, self.channel_7] ) / float(len([self.channel_6, self.channel_7])))
        self.freq_xlating_fir_filter_xxx_0_0_0_0_1.set_center_freq(self.channel_6 - self.center_freq_1)
        self.set_center_freq(sum([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12] ) / float(len([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12])))

    def get_channel_5(self):
        return self.channel_5

    def set_channel_5(self, channel_5):
        self.channel_5 = channel_5
        Qt.QMetaObject.invokeMethod(self._channel_5_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.channel_5)))
        self.set_center_freq(sum([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12] ) / float(len([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12])))

    def get_channel_4(self):
        return self.channel_4

    def set_channel_4(self, channel_4):
        self.channel_4 = channel_4
        Qt.QMetaObject.invokeMethod(self._channel_4_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.channel_4)))
        self.set_center_freq(sum([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12] ) / float(len([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12])))

    def get_channel_3(self):
        return self.channel_3

    def set_channel_3(self, channel_3):
        self.channel_3 = channel_3
        Qt.QMetaObject.invokeMethod(self._channel_3_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.channel_3)))
        self.set_center_freq(sum([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12] ) / float(len([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12])))

    def get_channel_2(self):
        return self.channel_2

    def set_channel_2(self, channel_2):
        self.channel_2 = channel_2
        Qt.QMetaObject.invokeMethod(self._channel_2_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.channel_2)))
        self.set_center_freq(sum([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12] ) / float(len([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12])))

    def get_channel_12(self):
        return self.channel_12

    def set_channel_12(self, channel_12):
        self.channel_12 = channel_12
        Qt.QMetaObject.invokeMethod(self._channel_12_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.channel_12)))
        self.set_center_freq(sum([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12] ) / float(len([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12])))

    def get_channel_11(self):
        return self.channel_11

    def set_channel_11(self, channel_11):
        self.channel_11 = channel_11
        Qt.QMetaObject.invokeMethod(self._channel_11_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.channel_11)))
        self.set_center_freq(sum([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12] ) / float(len([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12])))

    def get_channel_10(self):
        return self.channel_10

    def set_channel_10(self, channel_10):
        self.channel_10 = channel_10
        Qt.QMetaObject.invokeMethod(self._channel_10_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.channel_10)))
        self.set_center_freq(sum([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12] ) / float(len([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12])))

    def get_channel_1(self):
        return self.channel_1

    def set_channel_1(self, channel_1):
        self.channel_1 = channel_1
        Qt.QMetaObject.invokeMethod(self._channel_1_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.channel_1)))
        self.set_center_freq_0(sum([self.channel_0, self.channel_1] ) / float(len([self.channel_0, self.channel_1])))
        self.freq_xlating_fir_filter_xxx_0_0.set_center_freq(self.channel_1 - self.center_freq_0)
        self.set_center_freq(sum([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12] ) / float(len([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12])))

    def get_channel_0(self):
        return self.channel_0

    def set_channel_0(self, channel_0):
        self.channel_0 = channel_0
        Qt.QMetaObject.invokeMethod(self._channel_0_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.channel_0)))
        self.set_center_freq_0(sum([self.channel_0, self.channel_1] ) / float(len([self.channel_0, self.channel_1])))
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.channel_0 - self.center_freq_0)
        self.set_center_freq(sum([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12] ) / float(len([self.channel_0, self.channel_1, self.channel_2, self.channel_3, self.channel_4, self.channel_5, self.channel_6, self.channel_7, self.channel_8, self.channel_9, self.channel_10, self.channel_11, self.channel_12])))

    def get_xlate_filter_taps(self):
        return self.xlate_filter_taps

    def set_xlate_filter_taps(self, xlate_filter_taps):
        self.xlate_filter_taps = xlate_filter_taps

    def get_variable_qtgui_range_0(self):
        return self.variable_qtgui_range_0

    def set_variable_qtgui_range_0(self, variable_qtgui_range_0):
        self.variable_qtgui_range_0 = variable_qtgui_range_0

    def get_sqlch(self):
        return self.sqlch

    def set_sqlch(self, sqlch):
        self.sqlch = sqlch
        self.analog_pwr_squelch_xx_0_2.set_threshold(self.sqlch)
        self.analog_pwr_squelch_xx_0_0_1.set_threshold(self.sqlch)
        self.analog_pwr_squelch_xx_0_0_0_0_0_1.set_threshold(self.sqlch)
        self.analog_pwr_squelch_xx_0_0_0_0_0_0_0.set_threshold(self.sqlch)

    def get_if_gain(self):
        return self.if_gain

    def set_if_gain(self, if_gain):
        self.if_gain = if_gain
        self.osmosdr_source_0_0.set_if_gain(self.if_gain, 0)
        self.osmosdr_source_0.set_if_gain(self.if_gain, 0)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.osmosdr_source_0_0.set_gain(self.gain, 0)
        self.osmosdr_source_0.set_gain(self.gain, 0)

    def get_firdes_tap(self):
        return self.firdes_tap

    def set_firdes_tap(self, firdes_tap):
        self.firdes_tap = firdes_tap
        self.freq_xlating_fir_filter_xxx_0_0_0_0_1.set_taps((self.firdes_tap))
        self.freq_xlating_fir_filter_xxx_0_0_0_0_0_0.set_taps((self.firdes_tap))
        self.freq_xlating_fir_filter_xxx_0_0.set_taps((self.firdes_tap))
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.firdes_tap))

    def get_corr(self):
        return self.corr

    def set_corr(self, corr):
        self.corr = corr
        self.osmosdr_source_0_0.set_freq_corr(self.corr, 0)
        self.osmosdr_source_0.set_freq_corr(self.corr, 0)

    def get_channel_13(self):
        return self.channel_13

    def set_channel_13(self, channel_13):
        self.channel_13 = channel_13
        Qt.QMetaObject.invokeMethod(self._channel_13_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.channel_13)))

    def get_center_freq_1(self):
        return self.center_freq_1

    def set_center_freq_1(self, center_freq_1):
        self.center_freq_1 = center_freq_1
        self.osmosdr_source_0_0.set_center_freq(self.center_freq_1 - 100000, 0)
        self.freq_xlating_fir_filter_xxx_0_0_0_0_1.set_center_freq(self.channel_6 - self.center_freq_1)
        self.freq_xlating_fir_filter_xxx_0_0_0_0_0_0.set_center_freq(self.channel_7 - self.center_freq_1)

    def get_center_freq_0(self):
        return self.center_freq_0

    def set_center_freq_0(self, center_freq_0):
        self.center_freq_0 = center_freq_0
        self.osmosdr_source_0.set_center_freq(self.center_freq_0 - 100000, 0)
        self.freq_xlating_fir_filter_xxx_0_0.set_center_freq(self.channel_1 - self.center_freq_0)
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.channel_0 - self.center_freq_0)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq

    def get_bb_gain(self):
        return self.bb_gain

    def set_bb_gain(self, bb_gain):
        self.bb_gain = bb_gain
        self.osmosdr_source_0_0.set_bb_gain(self.bb_gain, 0)
        self.osmosdr_source_0.set_bb_gain(self.bb_gain, 0)


def main(top_block_cls=multimon_flex_rtl_tcp, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
