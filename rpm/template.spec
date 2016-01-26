Name:           ros-indigo-hironx-calibration
Version:        1.1.5
Release:        0%{?dist}
Summary:        ROS hironx_calibration package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/hironx_calibration
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-calibration-estimation
Requires:       ros-indigo-calibration-launch
Requires:       ros-indigo-kdl-parser
Requires:       ros-indigo-openni2-launch
Requires:       ros-indigo-orocos-kdl
BuildRequires:  ros-indigo-catkin

%description
Launch and configuration files for calibrating hironx using the new generic
'calibration' stack. THIS FILE IS AUTOMATICALLY GENERATED BY:
/home/k-okada/catkin_ws/ws_calibration/src/calibration/calibration_setup_helper/scripts/calibration_setup_helper.py
/home/k-okada/ros/hydro/src/rtm-ros-
robotics/rtmros_hironx/hironx_moveit_config/HiroNX.urdf --base-link
CHEST_JOINT0_Link --arm-tip-link RARM_JOINT5_Link --head-tip-link
HEAD_JOINT1_Link --arm-controller=rarm_controller/command --head-
controller=head_controller/command --head-camera-frame camera_rgb_optical_frame
--head-camera-joint head_to_kinect_joint

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Jan 26 2016 TORK <dev@opensource-robotics.tokyo.jp> - 1.1.5-0
- Autogenerated by Bloom

* Mon Jan 25 2016 TORK <dev@opensource-robotics.tokyo.jp> - 1.1.4-0
- Autogenerated by Bloom

* Wed Dec 16 2015 TORK <dev@opensource-robotics.tokyo.jp> - 1.1.3-0
- Autogenerated by Bloom

* Wed Nov 11 2015 TORK <dev@opensource-robotics.tokyo.jp> - 1.1.2-0
- Autogenerated by Bloom

* Mon Nov 02 2015 TORK <dev@opensource-robotics.tokyo.jp> - 1.1.1-0
- Autogenerated by Bloom

* Wed Oct 21 2015 TORK <dev@opensource-robotics.tokyo.jp> - 1.1.0-0
- Autogenerated by Bloom

* Fri Sep 11 2015 TORK <dev@opensource-robotics.tokyo.jp> - 1.0.37-0
- Autogenerated by Bloom

* Mon Aug 24 2015 TORK <dev@opensource-robotics.tokyo.jp> - 1.0.36-0
- Autogenerated by Bloom

* Fri Aug 14 2015 TORK <dev@opensource-robotics.tokyo.jp> - 1.0.35-0
- Autogenerated by Bloom

* Tue Aug 04 2015 TORK <dev@opensource-robotics.tokyo.jp> - 1.0.34-0
- Autogenerated by Bloom

* Thu Jul 30 2015 TORK <dev@opensource-robotics.tokyo.jp> - 1.0.33-0
- Autogenerated by Bloom

* Thu Jul 16 2015 TORK <dev@opensource-robotics.tokyo.jp> - 1.0.32-0
- Autogenerated by Bloom

* Sun May 31 2015 TORK <dev@opensource-robotics.tokyo.jp> - 1.0.31-0
- Autogenerated by Bloom

* Thu Apr 16 2015 TORK <dev@opensource-robotics.tokyo.jp> - 1.0.30-0
- Autogenerated by Bloom

* Mon Apr 06 2015 TORK <dev@opensource-robotics.tokyo.jp> - 1.0.29-0
- Autogenerated by Bloom

* Fri Feb 06 2015 Calibration Setup Helper <kei.okada@gmail.com> - 1.0.28-0
- Autogenerated by Bloom

