# Copyright (c) 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Launch realsense_ros2_camera node and rviz."""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():

    default_rviz = os.path.join(get_package_share_directory('realsense_ros2_camera'),
                                'launch', 'default.rviz')
    default_params = os.path.join(get_package_share_directory('realsense_ros2_camera'),
                                'params', 'params.yaml')
    return LaunchDescription([
        # Realsense
        launch_ros.actions.Node(
            package='realsense_ros2_camera', 
            executable='realsense_ros2_camera',
            name='realsense_ros2_camera_node',
            parameters=[default_params],
            output='screen')
    ])
