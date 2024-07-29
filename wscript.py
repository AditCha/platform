def options(opt):
    opt.load('compiler_c')

def configure(cfg):
    cfg.load('compiler_c')

def build(bld):
    # Find all C source files in the platform directory
    platform_driver_sources = bld.path.ant_glob([
        # Uncomment to enable driver
        # 'drivers/fpga_ip/Core10GBaseKR_PHY/*.c',
        # 'drivers/fpga_ip/CoreGPIO/*.c',
        # 'drivers/fpga_ip/CoreI2C/*.c',
        # 'drivers/fpga_ip/CoreMMC/*.c',
        # 'drivers/fpga_ip/CorePWM/*.c',
        # 'drivers/fpga_ip/CoreQSPI/*.c',
        # 'drivers/fpga_ip/CoreSPI/*.c',
        # 'drivers/fpga_ip/CoreSysServices_PF/*.c',
        # 'drivers/fpga_ip/CoreTSE/*.c',
        # 'drivers/fpga_ip/CoreTimer/*.c',
        # 'drivers/fpga_ip/CoreUARTapb/*.c',

        # 'drivers/mss/mss_can/*.c',
        # 'drivers/mss/mss_ethernet_mac/*.c',
        # 'drivers/mss/mss_gpio/*.c',
        # 'drivers/mss/mss_i2c/*.c',
        # 'drivers/mss/mss_mmc/*.c',
        'drivers/mss/mss_mmuart/*.c',
        # 'drivers/mss/mss_pdma/*.c',
        # 'drivers/mss/mss_qspi/*.c',
        # 'drivers/mss/mss_rtc/*.c',
        'drivers/mss/mss_spi/*.c',
        # 'drivers/mss/mss_sys_services/*.c',
        # 'drivers/mss/mss_timer/*.c',
        # 'drivers/mss/mss_usb/*.c',
        # 'drivers/mss/mss_watchdog/*.c',
        # 'drivers/mss/pf_pcie/*.c',

        'drivers/off_chip/*.c'
    ])

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
