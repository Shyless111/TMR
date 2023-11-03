JOINT_NAMES = {
    "smpljoints": [
        "pelvis",
        "left_hip",
        "right_hip",
        "spine1",
        "left_knee",
        "right_knee",
        "spine2",
        "left_ankle",
        "right_ankle",
        "spine3",
        "left_foot",
        "right_foot",
        "neck",
        "left_collar",
        "right_collar",
        "head",
        "left_shoulder",
        "right_shoulder",
        "left_elbow",
        "right_elbow",
        "left_wrist",
        "right_wrist",
        "left_hand",
        "right_hand",
    ],
    "guoh3djoints": [
        "pelvis",
        "left_hip",
        "right_hip",
        "spine1",
        "left_knee",
        "right_knee",
        "spine2",
        "left_ankle",
        "right_ankle",
        "spine3",
        "left_foot",
        "right_foot",
        "neck",
        "left_collar",
        "right_collar",
        "head",
        "left_shoulder",
        "right_shoulder",
        "left_elbow",
        "right_elbow",
        "left_wrist",
        "right_wrist",
    ],
}

INFOS = {
    "smpljoints": {
        "LM": JOINT_NAMES["smpljoints"].index("left_ankle"),
        "RM": JOINT_NAMES["smpljoints"].index("right_ankle"),
        "LF": JOINT_NAMES["smpljoints"].index("left_foot"),
        "RF": JOINT_NAMES["smpljoints"].index("right_foot"),
        "LS": JOINT_NAMES["smpljoints"].index("left_shoulder"),
        "RS": JOINT_NAMES["smpljoints"].index("right_shoulder"),
        "LH": JOINT_NAMES["smpljoints"].index("left_hip"),
        "RH": JOINT_NAMES["smpljoints"].index("right_hip"),
        "njoints": len(JOINT_NAMES["smpljoints"]),
    },
    "guoh3djoints": {
        "LM": JOINT_NAMES["guoh3djoints"].index("left_ankle"),
        "RM": JOINT_NAMES["guoh3djoints"].index("right_ankle"),
        "LF": JOINT_NAMES["guoh3djoints"].index("left_foot"),
        "RF": JOINT_NAMES["guoh3djoints"].index("right_foot"),
        "LS": JOINT_NAMES["guoh3djoints"].index("left_shoulder"),
        "RS": JOINT_NAMES["guoh3djoints"].index("right_shoulder"),
        "LH": JOINT_NAMES["guoh3djoints"].index("left_hip"),
        "RH": JOINT_NAMES["guoh3djoints"].index("right_hip"),
        "njoints": len(JOINT_NAMES["guoh3djoints"]),
    },
}
