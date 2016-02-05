Name:           ros-indigo-rtmros-hironx
Version:        1.1.7
Release:        0%{?dist}
Summary:        ROS rtmros_hironx package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rtmros_hironx/
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-hironx-calibration
Requires:       ros-indigo-hironx-moveit-config
Requires:       ros-indigo-hironx-ros-bridge
BuildRequires:  ros-indigo-catkin

%description
The rtmros_hironx package is an operating interface via ROS and OpenRTM, for
Hiro and NEXTAGE OPEN dual-armed robots from Kawada Industries Inc. NOTE for
Hiro users: Utilizing this opensource controller for Hiro requires installation
both on Controller Box (QNX-based) and Vision PC (Ubuntu Linux), and the steps
for it are not shared publicly in order to avoid any possible inconvenience that
can easily be caused by slight mis-operation during installation. Please contact
TORK for an advice.

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
* Fri Feb 05 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.7-0
- Autogenerated by Bloom

* Wed Feb 03 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.6-0
- Autogenerated by Bloom

* Tue Jan 26 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.5-0
- Autogenerated by Bloom

* Mon Jan 25 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.4-0
- Autogenerated by Bloom

* Wed Dec 16 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.3-0
- Autogenerated by Bloom

* Wed Nov 11 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.2-0
- Autogenerated by Bloom

* Mon Nov 02 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.1-0
- Autogenerated by Bloom

* Wed Oct 21 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.0-0
- Autogenerated by Bloom

* Fri Sep 11 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.37-0
- Autogenerated by Bloom

* Mon Aug 24 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.36-0
- Autogenerated by Bloom

* Fri Aug 14 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.35-0
- Autogenerated by Bloom

* Tue Aug 04 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.34-0
- Autogenerated by Bloom

* Thu Jul 30 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.33-0
- Autogenerated by Bloom

* Thu Jul 16 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.32-0
- Autogenerated by Bloom

* Sun May 31 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.31-0
- Autogenerated by Bloom

* Thu Apr 16 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.30-0
- Autogenerated by Bloom

* Mon Apr 06 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.29-0
- Autogenerated by Bloom

* Fri Feb 06 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.28-0
- Autogenerated by Bloom

