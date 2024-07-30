import configparser

def options(opt):
    opt.load('compiler_c')

def configure(cfg):
    cfg.load('compiler_c')

DRIVER_LOOK_UP= {
     'core10g'          : 'drivers/fpga_ip/Core10GBaseKR_PHY/*.c',
     'coreGPIO'         : 'drivers/fpga_ip/CoreGPIO/*.c',
     'coreI2C'          : 'drivers/fpga_ip/CoreI2C/*.c',
     'coreMMC'          : 'drivers/fpga_ip/CoreMMC/*.c',
     'corePWM'          : 'drivers/fpga_ip/CorePWM/*.c',
     'coreQSPI'         : 'drivers/fpga_ip/CoreQSPI/*.c',
     'coreSPI'          : 'drivers/fpga_ip/CoreSPI/*.c',
     'coreSysService'   : 'drivers/fpga_ip/CoreSysServices_PF/*.c',
     'coreTSE'          : 'drivers/fpga_ip/CoreTSE/*.c',
     'coreTimer'        : 'drivers/fpga_ip/CoreTimer/*.c',
     'coreUART'         : 'drivers/fpga_ip/CoreUARTapb/*.c',

     'CAN'              : 'drivers/mss/mss_can/*.c',
     'ETH'              : 'drivers/mss/mss_ethernet_mac/*.c',
     'GPIO'             : 'drivers/mss/mss_gpio/*.c',
     'I2C'              : 'drivers/mss/mss_i2c/*.c',
     'MMC'              : 'drivers/mss/mss_mmc/*.c',
     'UART'             : 'drivers/mss/mss_mmuart/*.c',
     'PDMA'             : 'drivers/mss/mss_pdma/*.c',
     'QSPI'             : 'drivers/mss/mss_qspi/*.c',
     'RTC'              : 'drivers/mss/mss_rtc/*.c',
     'SPI'              : 'drivers/mss/mss_spi/*.c',
     'SysService'       : 'drivers/mss/mss_sys_services/*.c',
     'Timer'            : 'drivers/mss/mss_timer/*.c',
     'USB'              : 'drivers/mss/mss_usb/*.c',
     'Watchdog'         : 'drivers/mss/mss_watchdog/*.c',
     'PCIE'             : 'drivers/mss/pf_pcie/*.c',
}

def build(bld):
    # Find all C source files in the platform directory
    cfg = configparser.ConfigParser()
    cfg.read(f'{bld.path}/../../usr_config.ini')
    plt = [DRIVER_LOOK_UP[k] for k in DRIVER_LOOK_UP.keys() if cfg.getboolean('driver',k,fallback=False)]
    platform_driver_sources = bld.path.ant_glob(plt)

    platform_c_sources = bld.path.ant_glob([
        'hal/**/*.c',
        'mpfs_hal/**/*.c'
    ])

    platform_asm_sources = bld.path.ant_glob([
        '**/*.S',
        '**/*.s'
    ])

   # platform_sources = platform_c_sources + platform_asm_sources + platform_driver_sources
    platform_sources = platform_c_sources +  platform_driver_sources
    # Create a static library for the platform code
    bld.stlib(
        target='libplatform',
        cflags = '-g -O2',
        includes = ['.',
                    'platform_config_reference',
                    '../boards/icicle-kit-es',
                    '../boards/icicle-kit-es/platform_config/lim-debug'],
        source=platform_sources,
    )
