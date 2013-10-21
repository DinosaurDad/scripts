#!/usr/bin/env python

def problematic_block(lba, first_part_sec, sec_size, blk_size):
    """Given the number (LBA) of a problematic sector on a disk, the number of
    the first sector of the partition that contains the LBA, the sector size
    of the disk and the block size of the filesystem, return the number of
    the filesystem block that contains the problematic sector.

    The number of the sector is usually found in a dmesg log or on the
    output of SMART checking tools, like `skdump` or `smartctl`.

    Example for a regular ext4 filesystem on a disk with 512-byte sectors:
    
    >>> problematic_block(1453654754, 499712, 512, 4096)
    181644380
    >>>
    """

    return (lba - first_part_sec) * sec_size // blk_size


def debugfs_discover_filename(blocknum, devnode):
    """Given a block number blocknum of an ext2/3/4 filesystem specified by
    devnode, try to find the name of the file in that filesystem that
    contains that block, if any.

    We assume that blocknum is a valid block number for the device devnode.

    We return None if the block is not associated with any file or return a
    list of strings containing the full path (absolute) for files that
    contain such block. Exception: the journal of the filesystem is
    represented as an empty string.

    One (unfortunate) use case of this function is to discover which files
    in an ext2/3/4 filesystem are affected by the problematic block given by
    blocknum.
    """
    pass

    # /home/rbrito/videos/Lectures/coursera/videos/COMPLETED/comnetworks-002/05_Week_5-_Routing/09_5-9_Hierarchical_Routing.mp4
    # dd if=/dev/zero of=/dev/sda2 bs=4096 count=1 seek=181644380
