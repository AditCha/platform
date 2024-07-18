# Find all C source files in the platform directory
file(GLOB_RECURSE PLATFORM_DRIVER_SOURCES
# Uncomment to enable driver
 #   "drivers/fpga_ip/Core10GBaseKR_PHY/*.c"
 #   "drivers/fpga_ip/CoreGPIO/*.c"
 #   "drivers/fpga_ip/CoreI2C/*.c"
 #   "drivers/fpga_ip/CoreMMC/*.c"
 #   "drivers/fpga_ip/CorePWM/*.c"
 #   "drivers/fpga_ip/CoreQSPI/*.c"
 #   "drivers/fpga_ip/CoreSPI/*.c"
 #   "drivers/fpga_ip/CoreSysServices_PF/*.c"
 #   "drivers/fpga_ip/CoreTSE/*.c"
 #   "drivers/fpga_ip/CoreTimer/*.c"
 #   "drivers/fpga_ip/CoreUARTapb/*.c"

 #   "drivers/mss/mss_can/*.c"
 #   "drivers/mss/mss_ethernet_mac/*.c"
 #   "drivers/mss/mss_gpio/*.c"
 #   "drivers/mss/mss_i2c/*.c"
 #   "drivers/mss/mss_mmc/*.c"
    "drivers/mss/mss_mmuart/*.c"
 #   "drivers/mss/mss_pdma/*.c"
 #   "drivers/mss/mss_qspi/*.c"
 #   "drivers/mss/mss_rtc/*.c"
 #   "drivers/mss/mss_spi/*.c"
 #   "drivers/mss/mss_sys_services/*.c"
 #   "drivers/mss/mss_timer/*.c"
 #   "drivers/mss/mss_usb/*.c"
 #   "drivers/mss/mss_watchdog/*.c"
 #   "drivers/mss/pf_pcie/*.c"

    "drivers/off_chip/*.c")

file(GLOB_RECURSE PLATFORM_C_SOURCES
    "hal/*.c"
    "mpfs_hal/*.c"
)

# Find all ASM source files in the platform directory
file(GLOB_RECURSE PLATFORM_ASM_SOURCES "*.S" "*.s")

set(PLATFORM_SOURCES ${PLATFORM_C_SOURCES} ${PLATFORM_ASM_SOURCES} ${PLATFORM_DRIVER_SOURCES})
# Create a static library for the platform code
add_custom_target(platform_module SOURCES ${PLATFORM_SOURCES})

set(PLATFORM_SOURCES ${PLATFORM_SOURCES} PARENT_SCOPE)
