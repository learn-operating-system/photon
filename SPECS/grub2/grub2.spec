%define debug_package %{nil}

Summary:    GRand Unified Bootloader
Name:       grub2
Version:    2.06
Release:    6%{?dist}
License:    GPLv3+
URL:        http://www.gnu.org/software/grub
Group:      Applications/System
Vendor:     VMware, Inc.
Distribution:   Photon

Source0: https://ftp.gnu.org/gnu/grub/grub-%{version}.tar.xz
%define sha512 grub=4f11c648f3078567e53fc0c74d5026fdc6da4be27d188975e79d9a4df817ade0fe5ad2ddd694238a07edc45adfa02943d83c57767dd51548102b375e529e8efe

%ifarch x86_64
Source1: grub2-2.06~rc1-grubx64.efi.gz
%define sha512 grub2-2.06~rc1-grubx64=d7530649ee0fe5a29809850ee27dde15d977e36a784407e74bcf2a42a6f56f9b30127392771b8c188dd271408b731318abefeb2a9704b6515dbf850efb0c2763
%endif

Patch0: Tweak-grub-mkconfig.in-to-work-better-in-Photon.patch

Patch1001: 0001-Revert-templates-Fix-user-facing-typo-with-an-incorr.patch
Patch1002: 0002-Revert-templates-Properly-disable-the-os-prober-by-d.patch
Patch1003: 0003-Revert-templates-Disable-the-os-prober-by-default.patch
Patch1004: 0004-Add-support-for-Linux-EFI-stub-loading.patch
Patch1005: 0005-Rework-linux-command.patch
Patch1006: 0006-Rework-linux16-command.patch
Patch1007: 0007-Add-secureboot-support-on-efi-chainloader.patch
Patch1008: 0008-Make-any-of-the-loaders-that-link-in-efi-mode-honor-.patch
Patch1009: 0009-Handle-multi-arch-64-on-32-boot-in-linuxefi-loader.patch
#Patch1010: 0010-re-write-.gitignore.patch
#Patch1011: 0011-IBM-client-architecture-CAS-reboot-support.patch
#Patch1012: 0012-for-ppc-reset-console-display-attr-when-clear-screen.patch
#Patch1013: 0013-Disable-GRUB-video-support-for-IBM-power-machines.patch
Patch1014: 0014-Move-bash-completion-script-922997.patch
Patch1015: 0015-Allow-fallback-to-include-entries-by-title-not-just-.patch
Patch1016: 0016-Make-exit-take-a-return-code.patch
Patch1017: 0017-Make-efi-machines-load-an-env-block-from-a-variable.patch
#Patch1018: 0018-Migrate-PPC-from-Yaboot-to-Grub2.patch
Patch1019: 0019-Add-fw_path-variable-revised.patch
Patch1020: 0020-Pass-x-hex-hex-straight-through-unmolested.patch
Patch1021: 0021-blscfg-add-blscfg-module-to-parse-Boot-Loader-Specif.patch
Patch1022: 0022-Add-devicetree-loading.patch
Patch1023: 0023-Enable-pager-by-default.-985860.patch
Patch1024: 0024-Don-t-say-GNU-Linux-in-generated-menus.patch
Patch1025: 0025-Add-.eh_frame-to-list-of-relocations-stripped.patch
Patch1026: 0026-Don-t-require-a-password-to-boot-entries-generated-b.patch
Patch1027: 0027-use-fw_path-prefix-when-fallback-searching-for-grub-.patch
Patch1028: 0028-Try-mac-guid-etc-before-grub.cfg-on-tftp-config-file.patch
Patch1029: 0029-Generate-OS-and-CLASS-in-10_linux-from-etc-os-releas.patch
Patch1030: 0030-Minimize-the-sort-ordering-for-.debug-and-rescue-ker.patch
Patch1031: 0031-Try-prefix-if-fw_path-doesn-t-work.patch
Patch1032: 0032-Make-grub2-mkconfig-construct-titles-that-look-like-.patch
#Patch1033: 0033-Add-friendly-grub2-password-config-tool-985962.patch
Patch1034: 0034-tcp-add-window-scaling-support.patch
Patch1035: 0035-efinet-and-bootp-add-support-for-dhcpv6.patch
Patch1036: 0036-Add-grub-get-kernel-settings-and-use-it-in-10_linux.patch
#Patch1037: 0037-bz1374141-fix-incorrect-mask-for-ppc64.patch
Patch1038: 0038-Make-grub_fatal-also-backtrace.patch
Patch1039: 0039-Make-our-info-pages-say-grub2-where-appropriate.patch
Patch1040: 0040-macos-just-build-chainloader-entries-don-t-try-any-x.patch
Patch1041: 0041-grub2-btrfs-Add-ability-to-boot-from-subvolumes.patch
Patch1042: 0042-export-btrfs_subvol-and-btrfs_subvolid.patch
Patch1043: 0043-grub2-btrfs-03-follow_default.patch
Patch1044: 0044-grub2-btrfs-04-grub2-install.patch
Patch1045: 0045-grub2-btrfs-05-grub2-mkconfig.patch
Patch1046: 0046-grub2-btrfs-06-subvol-mount.patch
Patch1047: 0047-Fallback-to-old-subvol-name-scheme-to-support-old-sn.patch
Patch1048: 0048-Grub-not-working-correctly-with-btrfs-snapshots-bsc-.patch
Patch1049: 0049-Add-grub_efi_allocate_pool-and-grub_efi_free_pool-wr.patch
Patch1050: 0050-Use-grub_efi_.-memory-helpers-where-reasonable.patch
Patch1051: 0051-Add-PRIxGRUB_EFI_STATUS-and-use-it.patch
Patch1052: 0052-don-t-use-int-for-efi-status.patch
Patch1053: 0053-make-GRUB_MOD_INIT-declare-its-function-prototypes.patch
Patch1054: 0054-Don-t-guess-boot-efi-as-HFS-on-ppc-machines-in-grub-.patch
Patch1055: 0055-20_linux_xen-load-xen-or-multiboot-2-modules-as-need.patch
Patch1056: 0056-Make-pmtimer-tsc-calibration-not-take-51-seconds-to-.patch
Patch1057: 0057-align-struct-efi_variable-better.patch
#Patch1058: 0058-Add-BLS-support-to-grub-mkconfig.patch
Patch1059: 0059-Don-t-attempt-to-backtrace-on-grub_abort-for-grub-em.patch
Patch1060: 0060-Add-linux-and-initrd-commands-for-grub-emu.patch
#Patch1061: 0061-Add-grub2-switch-to-blscfg.patch
Patch1062: 0062-make-better-backtraces.patch
Patch1063: 0063-normal-don-t-draw-our-startup-message-if-debug-is-se.patch
Patch1064: 0064-Work-around-some-minor-include-path-weirdnesses.patch
Patch1065: 0065-Make-it-possible-to-enabled-build-id-sha1.patch
Patch1066: 0066-Add-grub_qdprintf-grub_dprintf-without-the-file-line.patch
Patch1067: 0067-Make-a-gdb-dprintf-that-tells-us-load-addresses.patch
Patch1068: 0068-Fixup-for-newer-compiler.patch
Patch1069: 0069-Don-t-attempt-to-export-the-start-and-_start-symbols.patch
Patch1070: 0070-Fixup-for-newer-compiler.patch
Patch1071: 0071-Add-support-for-non-Ethernet-network-cards.patch
Patch1072: 0072-net-read-bracketed-ipv6-addrs-and-port-numbers.patch
Patch1073: 0073-bootp-New-net_bootp6-command.patch
Patch1074: 0074-efinet-UEFI-IPv6-PXE-support.patch
Patch1075: 0075-grub.texi-Add-net_bootp6-doument.patch
Patch1076: 0076-bootp-Add-processing-DHCPACK-packet-from-HTTP-Boot.patch
Patch1077: 0077-efinet-Setting-network-from-UEFI-device-path.patch
Patch1078: 0078-efinet-Setting-DNS-server-from-UEFI-protocol.patch
Patch1079: 0079-Support-UEFI-networking-protocols.patch
Patch1080: 0080-AUDIT-0-http-boot-tracker-bug.patch
Patch1081: 0081-grub-editenv-Add-incr-command-to-increment-integer-v.patch
#Patch1082: 0082-Add-auto-hide-menu-support.patch
Patch1083: 0083-Add-grub-set-bootflag-utility.patch
Patch1084: 0084-docs-Add-grub-boot-indeterminate.service-example.patch
Patch1085: 0085-gentpl-add-disable-support.patch
Patch1086: 0086-gentpl-add-pc-firmware-type.patch
Patch1087: 0087-efinet-also-use-the-firmware-acceleration-for-http.patch
Patch1088: 0088-efi-http-Make-root_url-reflect-the-protocol-hostname.patch
#Patch1089: 0089-Make-it-so-we-can-tell-configure-which-cflags-utils-.patch
Patch1090: 0090-module-verifier-make-it-possible-to-run-checkers-on-.patch
Patch1091: 0091-Rework-how-the-fdt-command-builds.patch
Patch1092: 0092-Disable-non-wordsize-allocations-on-arm.patch
Patch1093: 0093-Prepend-prefix-when-HTTP-path-is-relative.patch
Patch1094: 0094-Make-grub_error-more-verbose.patch
Patch1095: 0095-Make-reset-an-alias-for-the-reboot-command.patch
Patch1096: 0096-Add-a-version-command.patch
Patch1097: 0097-Add-more-dprintf-and-nerf-dprintf-in-script.c.patch
Patch1098: 0098-arm-arm64-loader-Better-memory-allocation-and-error-.patch
Patch1099: 0099-Try-to-pick-better-locations-for-kernel-and-initrd.patch
Patch1100: 0100-Attempt-to-fix-up-all-the-places-Wsign-compare-error.patch
Patch1101: 0101-Don-t-use-Wno-sign-compare-Wno-conversion-Wno-error-.patch
Patch1102: 0102-x86-efi-Use-bounce-buffers-for-reading-to-addresses-.patch
Patch1103: 0103-x86-efi-Re-arrange-grub_cmd_linux-a-little-bit.patch
Patch1104: 0104-x86-efi-Make-our-own-allocator-for-kernel-stuff.patch
Patch1105: 0105-x86-efi-Allow-initrd-params-cmdline-allocations-abov.patch
Patch1106: 0106-Fix-getroot.c-s-trampolines.patch
Patch1107: 0107-Do-not-allow-stack-trampolines-anywhere.patch
#Patch1108: 0108-Reimplement-boot_counter.patch
Patch1109: 0109-Fix-menu-entry-selection-based-on-ID-and-title.patch
Patch1110: 0110-Make-the-menu-entry-users-option-argument-to-be-opti.patch
Patch1111: 0111-Add-efi-export-env-and-efi-load-env-commands.patch
Patch1112: 0112-Make-it-possible-to-subtract-conditions-from-debug.patch
Patch1113: 0113-Export-all-variables-from-the-initial-context-when-c.patch
#Patch1114: 0114-grub.d-Split-out-boot-success-reset-from-menu-auto-h.patch
#Patch1115: 0115-Fix-systemctl-kexec-exit-status-check.patch
#Patch1116: 0116-Print-grub-emu-linux-loader-messages-as-debug.patch
Patch1117: 0117-Don-t-assume-that-boot-commands-will-only-return-on-.patch
Patch1118: 0118-grub-set-bootflag-Update-comment-about-running-as-ro.patch
Patch1119: 0119-grub-set-bootflag-Write-new-env-to-tmpfile-and-then-.patch
#Patch1120: 0120-grub.d-Fix-boot_indeterminate-getting-set-on-boot_su.patch
Patch1121: 0121-Add-start-symbol-for-RISC-V.patch
#Patch1122: 0122-bootstrap.conf-Force-autogen.sh-to-use-python3.patch
Patch1123: 0123-efi-http-Export-fw-http-_path-variables-to-make-them.patch
Patch1124: 0124-efi-http-Enclose-literal-IPv6-addresses-in-square-br.patch
Patch1125: 0125-efi-net-Allow-to-specify-a-port-number-in-addresses.patch
Patch1126: 0126-efi-ip4_config-Improve-check-to-detect-literal-IPv6-.patch
Patch1127: 0127-efi-net-Print-a-debug-message-if-parsing-the-address.patch
Patch1128: 0128-kern-term-Also-accept-F8-as-a-user-interrupt-key.patch
Patch1129: 0129-efi-Set-image-base-address-before-jumping-to-the-PE-.patch
Patch1130: 0130-tpm-Don-t-propagate-TPM-measurement-errors-to-the-ve.patch
Patch1131: 0131-x86-efi-Reduce-maximum-bounce-buffer-size-to-16-MiB.patch
Patch1132: 0132-http-Prepend-prefix-when-the-HTTP-path-is-relative-a.patch
Patch1133: 0133-Fix-a-missing-return-in-efi-export-env-and-efi-load-.patch
Patch1134: 0134-efi-dhcp-fix-some-allocation-error-checking.patch
Patch1135: 0135-efi-http-fix-some-allocation-error-checking.patch
Patch1136: 0136-efi-ip-46-_config.c-fix-some-potential-allocation-ov.patch
Patch1137: 0137-efilinux-Fix-integer-overflows-in-grub_cmd_initrd.patch
Patch1138: 0138-linuxefi-fail-kernel-validation-without-shim-protoco.patch
Patch1139: 0139-Fix-const-char-pointers-in-grub-core-net-bootp.c.patch
Patch1140: 0140-Fix-const-char-pointers-in-grub-core-net-efi-ip4_con.patch
Patch1141: 0141-Fix-const-char-pointers-in-grub-core-net-efi-ip6_con.patch
Patch1142: 0142-Fix-const-char-pointers-in-grub-core-net-efi-net.c.patch
Patch1143: 0143-Fix-const-char-pointers-in-grub-core-net-efi-pxe.c.patch
#Patch1144: 0144-Add-systemd-integration-scripts-to-make-systemctl-re.patch
#Patch1145: 0145-systemd-integration.sh-Also-set-old-menu_show_once-g.patch
Patch1146: 0146-at_keyboard-use-set-1-when-keyboard-is-in-Translate-.patch
Patch1147: 0147-grub-install-disable-support-for-EFI-platforms.patch
Patch1148: 0148-New-with-debug-timestamps-configure-flag-to-prepend-.patch
Patch1149: 0149-Added-debug-statements-to-grub_disk_open-and-grub_di.patch
Patch1150: 0150-Introduce-function-grub_debug_is_enabled-void-return.patch
Patch1151: 0151-Don-t-clear-screen-when-debugging-is-enabled.patch
Patch1152: 0152-kern-file-Fix-error-handling-in-grub_file_open.patch
Patch1153: 0153-grub_file_-instrumentation-new-file-debug-tag.patch
#Patch1154: 0154-ieee1275-Avoiding-many-unecessary-open-close.patch
#Patch1155: 0155-ieee1275-powerpc-implements-fibre-channel-discovery-.patch
#Patch1156: 0156-ieee1275-powerpc-enables-device-mapper-discovery.patch
Patch1157: 0157-Add-at_keyboard_fallback_set-var-to-force-the-set-ma.patch
Patch1158: 0158-Add-suport-for-signing-grub-with-an-appended-signatu.patch
Patch1159: 0159-docs-grub-Document-signing-grub-under-UEFI.patch
Patch1160: 0160-docs-grub-Document-signing-grub-with-an-appended-sig.patch
Patch1161: 0161-dl-provide-a-fake-grub_dl_set_persistent-for-the-emu.patch
Patch1162: 0162-pgp-factor-out-rsa_pad.patch
Patch1163: 0163-crypto-move-storage-for-grub_crypto_pk_-to-crypto.c.patch
Patch1164: 0164-posix_wrap-tweaks-in-preparation-for-libtasn1.patch
Patch1165: 0165-libtasn1-import-libtasn1-4.16.0.patch
Patch1166: 0166-libtasn1-disable-code-not-needed-in-grub.patch
Patch1167: 0167-libtasn1-changes-for-grub-compatibility.patch
Patch1168: 0168-libtasn1-compile-into-asn1-module.patch
#Patch1169: 0169-test_asn1-test-module-for-libtasn1.patch
Patch1170: 0170-grub-install-support-embedding-x509-certificates.patch
Patch1171: 0171-appended-signatures-import-GNUTLS-s-ASN.1-descriptio.patch
Patch1172: 0172-appended-signatures-parse-PKCS-7-signedData-and-X.50.patch
Patch1173: 0173-appended-signatures-support-verifying-appended-signa.patch
Patch1174: 0174-appended-signatures-verification-tests.patch
Patch1175: 0175-appended-signatures-documentation.patch
#Patch1176: 0176-ieee1275-enter-lockdown-based-on-ibm-secure-boot.patch
#Patch1177: 0177-ieee1275-drop-HEAP_MAX_ADDR-HEAP_MIN_SIZE.patch
#Patch1178: 0178-ieee1275-claim-more-memory.patch
#Patch1179: 0179-ieee1275-request-memory-with-ibm-client-architecture.patch
Patch1180: 0180-appendedsig-x509-Also-handle-the-Extended-Key-Usage-.patch
#Patch1181: 0181-ieee1275-ofdisk-retry-on-open-failure.patch
Patch1182: 0182-Allow-chainloading-EFI-apps-from-loop-mounts.patch
Patch1183: 0183-efinet-Add-DHCP-proxy-support.patch
Patch1184: 0184-fs-ext2-Ignore-checksum-seed-incompat-feature.patch
#Patch1185: 0185-Don-t-update-the-cmdline-when-generating-legacy-menu.patch
Patch1186: 0186-Suppress-gettext-error-message.patch
#Patch1187: 0187-grub-set-password-Always-use-boot-grub2-user.cfg-as-.patch
Patch1188: 0188-templates-Check-for-EFI-at-runtime-instead-of-config.patch
Patch1189: 0189-efi-Print-an-error-if-boot-to-firmware-setup-is-not-.patch
Patch1190: 0190-arm64-Fix-EFI-loader-kernel-image-allocation.patch
Patch1191: 0191-normal-main-Discover-the-device-to-read-the-config-f.patch
#Patch1192: 0192-powerpc-adjust-setting-of-prefix-for-signed-binary-c.patch
Patch1193: 0193-fs-xfs-Fix-unreadable-filesystem-with-v4-superblock.patch
Patch1194: 0194-Print-module-name-on-license-check-failure.patch
#Patch1195: 0195-powerpc-ieee1275-load-grub-at-4MB-not-2MB.patch
Patch1196: 0196-grub-mkconfig-restore-umask-for-grub.cfg.patch
Patch1197: 0197-fs-btrfs-Use-full-btrfs-bootloader-area.patch
Patch1198: 0198-Add-Fedora-location-of-DejaVu-SANS-font.patch
Patch1199: 0199-normal-menu-Don-t-show-Booting-s-msg-when-auto-booti.patch
Patch1200: 0200-EFI-suppress-the-Welcome-to-GRUB-message-in-EFI-buil.patch
Patch1201: 0201-EFI-console-Do-not-set-colorstate-until-the-first-te.patch
Patch1202: 0202-EFI-console-Do-not-set-cursor-until-the-first-text-o.patch
Patch1203: 0203-Use-visual-indentation-in-config.h.in.patch
Patch1204: 0204-Where-present-ensure-config-util.h-precedes-config.h.patch
#Patch1205: 0205-Drop-gnulib-fix-base64.patch.patch
#Patch1206: 0206-Drop-gnulib-no-abort.patch.patch
#Patch1207: 0207-Update-gnulib-version-and-drop-most-gnulib-patches.patch
Patch1208: 0208-commands-search-Fix-bug-stopping-iteration-when-no-f.patch
Patch1209: 0209-search-new-efidisk-only-option-on-EFI-systems.patch
Patch1210: 0210-efi-new-connectefi-command.patch
Patch1211: 0211-grub-core-loader-i386-efi-linux.c-do-not-validate-ke.patch
Patch1212: 0212-grub-core-loader-arm64-linux.c-do-not-validate-kerne.patch
Patch1213: 0213-grub-core-loader-efi-chainloader.c-do-not-validate-c.patch
Patch1214: 0214-grub-core-loader-efi-linux.c-drop-now-unused-grub_li.patch
#Patch1215: 0215-powerpc-do-CAS-in-a-more-compatible-way.patch
#Patch1216: 0216-powerpc-prefix-detection-support-device-names-with-c.patch
#Patch1217: 0217-ibmvtpm-Add-support-for-trusted-boot-using-a-vTPM-2..patch
#Patch1218: 0218-make-ofdisk_retries-optional.patch
Patch1219: 0219-loader-efi-chainloader-grub_load_and_start_image-doe.patch
Patch1220: 0220-loader-efi-chainloader-simplify-the-loader-state.patch
Patch1221: 0221-commands-boot-Add-API-to-pass-context-to-loader.patch
Patch1222: 0222-loader-efi-chainloader-Use-grub_loader_set_ex.patch
Patch1223: 0223-loader-i386-efi-linux-Avoid-a-use-after-free-in-the-.patch
Patch1224: 0224-loader-i386-efi-linux-Use-grub_loader_set_ex.patch
Patch1225: 0225-loader-i386-efi-linux-Fix-a-memory-leak-in-the-initr.patch

# CVE-2022-2601 patch series
Patch1226: 0226-kern-efi-sb-Reject-non-kernel-files-in-the-shim_lock.patch

Patch1227: 0227-kern-file-Do-not-leak-device_name-on-error-in-grub_f.patch
Patch1228: 0228-video-readers-png-Abort-sooner-if-a-read-operation-f.patch
Patch1229: 0229-video-readers-png-Refuse-to-handle-multiple-image-he.patch
Patch1230: 0230-video-readers-png-Drop-greyscale-support-to-fix-heap.patch
Patch1231: 0231-video-readers-png-Avoid-heap-OOB-R-W-inserting-huff-.patch
Patch1232: 0232-video-readers-png-Sanity-check-some-huffman-codes.patch
Patch1233: 0233-video-readers-jpeg-Abort-sooner-if-a-read-operation-.patch
Patch1234: 0234-video-readers-jpeg-Do-not-reallocate-a-given-huff-ta.patch
Patch1235: 0235-video-readers-jpeg-Refuse-to-handle-multiple-start-o.patch
Patch1236: 0236-video-readers-jpeg-Block-int-underflow-wild-pointer-.patch

# CVE-2022-2601 patch series
Patch1237: 0237-normal-charset-Fix-array-out-of-bounds-formatting-un.patch

Patch1238: 0238-net-netbuff-Block-overly-large-netbuff-allocs.patch
Patch1239: 0239-net-ip-Do-IP-fragment-maths-safely.patch
Patch1240: 0240-net-dns-Fix-double-free-addresses-on-corrupt-DNS-res.patch
Patch1241: 0241-net-dns-Don-t-read-past-the-end-of-the-string-we-re-.patch
Patch1242: 0242-net-tftp-Prevent-a-UAF-and-double-free-from-a-failed.patch
Patch1243: 0243-net-tftp-Avoid-a-trivial-UAF.patch
Patch1244: 0244-net-http-Do-not-tear-down-socket-if-it-s-already-bee.patch
Patch1245: 0245-net-http-Fix-OOB-write-for-split-http-headers.patch
Patch1246: 0246-net-http-Error-out-on-headers-with-LF-without-CR.patch
Patch1247: 0247-fs-f2fs-Do-not-read-past-the-end-of-nat-journal-entr.patch
Patch1248: 0248-fs-f2fs-Do-not-read-past-the-end-of-nat-bitmap.patch
Patch1249: 0249-fs-f2fs-Do-not-copy-file-names-that-are-too-long.patch
Patch1250: 0250-fs-btrfs-Fix-several-fuzz-issues-with-invalid-dir-it.patch
Patch1251: 0251-fs-btrfs-Fix-more-ASAN-and-SEGV-issues-found-with-fu.patch
Patch1252: 0252-fs-btrfs-Fix-more-fuzz-issues-related-to-chunks.patch
Patch1253: 0253-misc-Make-grub_min-and-grub_max-more-resilient.patch
Patch1254: 0254-ReiserFS-switch-to-using-grub_min-grub_max.patch
Patch1255: 0255-misc-make-grub_boot_time-also-call-grub_dprintf-boot.patch
Patch1256: 0256-modules-make-.module_license-read-only.patch
Patch1257: 0257-modules-strip-.llvm_addrsig-sections-and-similar.patch
Patch1258: 0258-modules-Don-t-allocate-space-for-non-allocable-secti.patch
Patch1259: 0259-pe-add-the-DOS-header-struct-and-fix-some-bad-naming.patch
Patch1260: 0260-EFI-allocate-kernel-in-EFI_RUNTIME_SERVICES_CODE-ins.patch
Patch1261: 0261-modules-load-module-sections-at-page-aligned-address.patch
Patch1262: 0262-nx-add-memory-attribute-get-set-API.patch
Patch1263: 0263-nx-set-page-permissions-for-loaded-modules.patch
Patch1264: 0264-nx-set-attrs-in-our-kernel-loaders.patch
Patch1265: 0265-nx-set-the-nx-compatible-flag-in-EFI-grub-images.patch
Patch1266: 0266-grub-probe-document-the-behavior-of-multiple-v.patch
Patch1267: 0267-grub_fs_probe-dprint-errors-from-filesystems.patch
Patch1268: 0268-fs-fat-don-t-error-when-mtime-is-0.patch
Patch1269: 0269-Make-debug-file-show-which-file-filters-get-run.patch
Patch1270: 0270-efi-use-enumerated-array-positions-for-our-allocatio.patch
Patch1271: 0271-efi-split-allocation-policy-for-kernel-vs-initrd-mem.patch
Patch1272: 0272-efi-allocate-the-initrd-within-the-bounds-expressed-.patch
Patch1273: 0273-efi-use-EFI_LOADER_-CODE-DATA-for-kernel-and-initrd-.patch
#Patch1274: 0274-BLS-create-etc-kernel-cmdline-during-mkconfig.patch
#Patch1275: 0275-squish-don-t-dup-rhgb-quiet-check-mtimes.patch
#Patch1276: 0276-squish-give-up-on-rhgb-quiet.patch
#Patch1277: 0277-squish-BLS-only-write-etc-kernel-cmdline-if-writable.patch
#Patch1278: 0278-ieee1275-implement-vec5-for-cas-negotiation.patch
Patch1279: 0279-blscfg-Don-t-root-device-in-emu-builds.patch
Patch1280: 0280-loader-arm64-linux-Remove-magic-number-header-field-.patch
Patch1281: 0281-Correct-BSS-zeroing-on-aarch64.patch
Patch1282: 0282-linuxefi-Invalidate-i-cache-before-starting-the-kern.patch
Patch1283: 0283-x86-efi-Fix-an-incorrect-array-size-in-kernel-alloca.patch
Patch1284: 0284-commands-efi-tpm-Refine-the-status-of-log-event.patch
Patch1285: 0285-commands-efi-tpm-Use-grub_strcpy-instead-of-grub_mem.patch
Patch1286: 0286-efi-tpm-Add-EFI_CC_MEASUREMENT_PROTOCOL-support.patch

# CVE-2022-2601 patch series
Patch1287: 0287-font-Reject-glyphs-exceeds-font-max_glyph_width-or-f.patch
Patch1288: 0288-font-Fix-size-overflow-in-grub_font_get_glyph_intern.patch
Patch1289: 0289-font-Fix-several-integer-overflows-in-grub_font_cons.patch
Patch1290: 0290-font-Remove-grub_font_dup_glyph.patch
Patch1291: 0291-font-Fix-integer-overflow-in-ensure_comb_space.patch
Patch1292: 0292-font-Fix-integer-overflow-in-BMP-index.patch
Patch1293: 0293-font-Fix-integer-underflow-in-binary-search-of-char-.patch
Patch1294: 0294-kern-efi-sb-Enforce-verification-of-font-files.patch
Patch1295: 0295-fbutil-Fix-integer-overflow.patch
Patch1296: 0296-font-Fix-an-integer-underflow-in-blit_comb.patch
Patch1297: 0297-font-Harden-grub_font_blit_glyph-and-grub_font_blit_.patch
Patch1298: 0298-font-Assign-null_font-to-glyphs-in-ascii_font_glyph.patch
Patch1299: 0299-normal-charset-Fix-an-integer-overflow-in-grub_unico.patch

Patch1300: 0300-font-Try-opening-fonts-from-the-bundled-memdisk.patch
#Patch1301: 0301-Correction-in-vector-5-values.patch
Patch1302: 0302-mm-Clarify-grub_real_malloc.patch
Patch1303: 0303-mm-grub_real_malloc-Make-small-allocs-comment-match-.patch
Patch1304: 0304-mm-Document-grub_free.patch
Patch1305: 0305-mm-Document-grub_mm_init_region.patch
Patch1306: 0306-mm-Document-GRUB-internal-memory-management-structur.patch
Patch1307: 0307-mm-Assert-that-we-preserve-header-vs-region-alignmen.patch
Patch1308: 0308-mm-When-adding-a-region-merge-with-region-after-as-w.patch
Patch1309: 0309-mm-Debug-support-for-region-operations.patch
Patch1310: 0310-mm-Drop-unused-unloading-of-modules-on-OOM.patch
Patch1311: 0311-mm-Allow-dynamically-requesting-additional-memory-re.patch
Patch1312: 0312-kern-efi-mm-Always-request-a-fixed-number-of-pages-o.patch
Patch1313: 0313-kern-efi-mm-Extract-function-to-add-memory-regions.patch
Patch1314: 0314-kern-efi-mm-Pass-up-errors-from-add_memory_regions.patch
Patch1315: 0315-kern-efi-mm-Implement-runtime-addition-of-pages.patch
Patch1316: 0316-efi-Increase-default-memory-allocation-to-32-MiB.patch
Patch1317: 0317-mm-Try-invalidate-disk-caches-last-when-out-of-memor.patch
#Patch1318: 0318-ppc64le-signed-boot-media-changes.patch

BuildRequires:  device-mapper-devel
BuildRequires:  xz-devel
BuildRequires:  systemd-devel
BuildRequires:  bison

Requires:   xz-libs
Requires:   device-mapper-libs
Requires:   systemd-udev

%description
The GRUB package contains the GRand Unified Bootloader.

%package lang
Summary:    Additional language files for grub
Group:      System Environment/Programming
Requires:   %{name} = %{version}-%{release}
%description lang
These are the additional language files of grub.

%ifarch x86_64
%package pc
Summary:    GRUB Library for BIOS
Group:      System Environment/Programming
Requires:   %{name} = %{version}-%{release}
%description pc
Additional library files for grub
%endif

%package efi
Summary:    GRUB Library for UEFI
Group:      System Environment/Programming
Requires:   %{name} = %{version}-%{release}
%description efi
Additional library files for grub

%package efi-image
Summary:    GRUB UEFI image
Group:      System Environment/Base
%ifarch x86_64
Requires:   shim-signed >= 15.4
%endif
%description efi-image
GRUB UEFI image signed by vendor key

%prep
%autosetup -p1 -n grub-%{version}

%build
sh ./autogen.sh
%ifarch x86_64
mkdir -p build-for-pc
pushd build-for-pc
sh ../configure \
    --prefix=%{_prefix} \
    --sbindir=%{_sbindir} \
    --sysconfdir=%{_sysconfdir} \
    --disable-werror \
    --disable-efiemu \
    --disable-nls \
    --with-grubdir=grub2 \
    --with-platform=pc \
    --target=i386 \
    --program-transform-name=s,grub,%{name}, \
    --with-bootdir="/boot"

make %{?_smp_mflags}

make DESTDIR=${PWD}/../install-for-pc install %{?_smp_mflags}
popd
%endif

mkdir -p build-for-efi
pushd build-for-efi
sh ../configure \
    --prefix=%{_prefix} \
    --sbindir=%{_sbindir} \
    --sysconfdir=%{_sysconfdir} \
    --disable-werror \
    --disable-efiemu \
    --with-grubdir=grub2 \
    --with-platform=efi \
    --target=%{_arch} \
    --program-transform-name=s,grub,%{name}, \
    --with-bootdir="/boot"

make %{?_smp_mflags}

make DESTDIR=${PWD}/../install-for-efi install %{?_smp_mflags}
popd

%install
mkdir -p %{buildroot}%{_sysconfdir}/default \
         %{buildroot}%{_sysconfdir}/sysconfig \
         %{buildroot}/boot/%{name}

cp -apr install-for-efi/. %{buildroot}/.
%ifarch x86_64
cp -apr install-for-pc/. %{buildroot}/.
%endif
touch %{buildroot}%{_sysconfdir}/default/grub
ln -sf %{_sysconfdir}/default/grub %{buildroot}%{_sysconfdir}/sysconfig/grub
touch %{buildroot}/boot/%{name}/grub.cfg
rm -rf %{buildroot}%{_infodir}
# Generate grub efi image
install -d %{buildroot}/boot/efi/EFI/BOOT
%ifarch x86_64
# Use presigned image from tarball as of now.
gunzip -c %{SOURCE1} > %{buildroot}/boot/efi/EFI/BOOT/grubx64.efi
# The image was created by following commands:

#cat << EOF > grub-sbat.csv
#sbat,1,SBAT Version,sbat,1,https://github.com/rhboot/shim/blob/main/SBAT.md
#grub,1,Free Software Foundation,grub,2.06~rc1,https//www.gnu.org/software/grub/
#grub.photon,1,VMware Photon OS,grub2,2.06~rc1-1.ph4,https://github.com/vmware/photon/tree/4.0/SPECS/grub2/
#EOF
#
#grub2-mkimage -d /usr/lib/grub/x86_64-efi/ -o grubx64.efi -p /boot/grub2 -O x86_64-efi --sbat=grub-sbat.csv fat iso9660 part_gpt part_msdos normal boot linux configfile loopback chain efifwsetup efi_gop efi_uga ls search search_label search_fs_uuid search_fs_file gfxterm gfxterm_background gfxterm_menu test all_video loadenv exfat ext2 udf halt gfxmenu png tga lsefi help probe echo lvm

# Local alternative:
# ./install-for-efi/usr/bin/grub2-mkimage -d ./install-for-efi/usr/lib/grub/x86_64-efi/ -o %{buildroot}/boot/efi/EFI/BOOT/grubx64.efi -p /boot/grub2 -O x86_64-efi --sbat=grub-sbat.csv fat iso9660 part_gpt part_msdos normal boot linux configfile loopback chain efifwsetup efi_gop efi_uga ls search search_label search_fs_uuid search_fs_file gfxterm gfxterm_background gfxterm_menu test all_video loadenv exfat ext2 udf halt gfxmenu png tga lsefi help probe echo lvm

%endif
%ifarch aarch64
cat > grub-embed-config.cfg << EOF
search.fs_label rootfs root
configfile /boot/grub2/grub.cfg
EOF

./install-for-efi/usr/bin/grub2-mkimage -d ./install-for-efi/usr/lib/grub/arm64-efi/ -o %{buildroot}/boot/efi/EFI/BOOT/bootaa64.efi -p /boot/grub2 -O arm64-efi -c grub-embed-config.cfg fat iso9660 part_gpt part_msdos  normal boot linux configfile loopback chain efifwsetup efi_gop efinet ls search search_label search_fs_uuid search_fs_file  gfxterm gfxterm_background gfxterm_menu test all_video loadenv  exfat ext2 udf halt gfxmenu png tga lsefi help all_video probe echo
%endif

%if 0%{?with_check}
# make sure all files are same between two configure except the /usr/lib/grub
%check
%ifarch x86_64
diff -sr install-for-efi/sbin install-for-pc/sbin
diff -sr install-for-efi%{_bindir} install-for-pc%{_bindir}
diff -sr install-for-efi%{_sysconfdir} install-for-pc%{_sysconfdir}
diff -sr install-for-efi%{_datarootdir} install-for-pc%{_datarootdir}
%endif
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/grub.d
%config() %{_sysconfdir}/grub.d/00_header
%config() %{_sysconfdir}/grub.d/10_linux
%config() %{_sysconfdir}/grub.d/20_linux_xen
%config() %{_sysconfdir}/grub.d/30_os-prober
%config() %{_sysconfdir}/grub.d/30_uefi-firmware
%config(noreplace) %{_sysconfdir}/grub.d/40_custom
%config(noreplace) %{_sysconfdir}/grub.d/41_custom
%{_sysconfdir}/grub.d/README
%{_sbindir}/*
%{_bindir}/*
%{_datarootdir}/bash-completion/completions/grub
%{_datarootdir}/grub/*
%{_sysconfdir}/sysconfig/grub
%{_sysconfdir}/default/grub
%ghost %config(noreplace) /boot/%{name}/grub.cfg

%ifarch x86_64
%files pc
%defattr(-,root,root)
%{_libdir}/grub/i386-pc

%files efi
%defattr(-,root,root)
%{_libdir}/grub/x86_64-efi
%endif

%ifarch aarch64
%files efi
%defattr(-,root,root)
%{_libdir}/grub/*
%endif

%files efi-image
%defattr(-,root,root)
/boot/efi/EFI/BOOT/*

%files lang
%defattr(-,root,root)
%{_datarootdir}/locale/*

%changelog
* Wed Feb 15 2023 Alexey Makhalov <amakhalov@vmware.com> 2.06-6
- Go back to Fedora/RHEL style of SecureBoot with their latest features
  such as NX_COMPAT and security fixes.
* Fri Dec 23 2022 Oliver Kurth <okurth@vmware.com> 2.06-5
- bump version as a part of xz upgrade
* Tue Dec 20 2022 Shreenidhi Shedi <sshedi@vmware.com> 2.06-4
- Fix CVE-2022-2601
* Thu Jun 09 2022 Shreenidhi Shedi <sshedi@vmware.com> 2.06-3
- Add systemd-udev to Requires
* Wed Aug 18 2021 Ankit Jain <ankitja@vmware.com> 2.06-2
- Remove prompt message for default -o option in grub2-mkconfig
* Wed Jun 16 2021 Shreenidhi Shedi <sshedi@vmware.com> 2.06-1
- Upgrade to version 2.06
* Wed Apr 28 2021 Alexey Makhalov <amakhalov@vmware.com> 2.06~rc1-2
- Update signed grubx64.efi with recent fixes and SBAT support.
* Mon Mar 15 2021 Ajay Kaher <akaher@vmware.com> 2.06~rc1-1
- upgrade to 2.06.rc1-1
* Mon Mar 01 2021 Alexey Makhalov <amakhalov@vmware.com> 2.04-3
- Fixes for CVE-2020-14372, CVE-2020-25632, CVE-2020-25647,
  CVE-2020-27749, CVE-2020-27779, CVE-2021-3418, CVE-2021-20225,
  CVE-2021-20233.
* Fri Oct 30 2020 Bo Gan <ganb@vmware.com> 2.04-2
- Fix boot failure on aarch64
- ERROR: (FIRMWARE BUG: efi_loaded_image_t::image_base has bogus value)
* Thu Oct 29 2020 Alexey Makhalov <amakhalov@vmware.com> 2.04-1
- Fixes for CVE-2020-10713, CVE-2020-14308, CVE-2020-14309,
  CVE-2020-14310, CVE-2020-14311, CVE-2020-15705, CVE-2020-15706
  CVE-2020-15707.
* Mon Oct 26 2020 Alexey Makhalov <amakhalov@vmware.com> 2.02-15
- Use prebuilt and presigned grubx64.efi.
* Tue Mar 10 2020 Alexey Makhalov <amakhalov@vmware.com> 2.02-14
- Package grubx64.efi (bootaa64.efi) into -efi-image subpackage.
* Wed Aug 14 2019 Alexey Makhalov <amakhalov@vmware.com> 2.02-13
- Add one more patch from fc30 to fix arm64 build.
* Thu Feb 21 2019 Alexey Makhalov <amakhalov@vmware.com> 2.02-12
- Update grub version from ~rc3 to release.
- Enhance SB + TPM support (19 patches from grub2-2.02-70.fc30)
- Remove i386-pc modules from grub2-efi
* Fri Jan 25 2019 Alexey Makhalov <amakhalov@vmware.com> 2.02-11
- Disable efinet for aarch64 to workwround NXP ls1012a frwy PFE bug.
* Tue Nov 14 2017 Alexey Makhalov <amakhalov@vmware.com> 2.02-10
- Aarch64 support
* Fri Jun 2  2017 Bo Gan <ganb@vmware.com> 2.02-9
- Split grub2 to grub2 and grub2-pc, remove grub2-efi spec
* Fri Apr 14 2017 Alexey Makhalov <amakhalov@vmware.com>  2.02-8
- Version update to 2.02~rc2
* Fri Nov 18 2016 Anish Swaminathan <anishs@vmware.com>  2.02-7
- Add fix for CVE-2015-8370
* Fri Nov 18 2016 Anish Swaminathan <anishs@vmware.com>  2.02-6
- Change systemd dependency
* Thu Oct 06 2016 ChangLee <changlee@vmware.com> 2.02-5
- Modified %check
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 2.02-4
- GA - Bump release of all rpms
* Fri Oct 02 2015 Divya Thaluru <dthaluru@vmware.com> 2.02-3
- Adding patch to boot entries with out password.
* Wed Jul 22 2015 Divya Thaluru <dthaluru@vmware.com> 2.02-2
- Changing program name from grub to grub2.
* Mon Jun 29 2015 Divya Thaluru <dthaluru@vmware.com> 2.02-1
- Updating grub to 2.02
* Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 2.00-1
- Initial build.  First version
