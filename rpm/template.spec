Name:           ros-melodic-schunk-sdh
Version:        0.6.13
Release:        2%{?dist}
Summary:        ROS schunk_sdh package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://ros.org/wiki/schunk_sdh
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python2-devel
Requires:       boost-python3-devel
Requires:       dpkg
Requires:       libusb-devel
Requires:       ros-melodic-actionlib
Requires:       ros-melodic-cob-srvs
Requires:       ros-melodic-control-msgs
Requires:       ros-melodic-diagnostic-msgs
Requires:       ros-melodic-libntcan
Requires:       ros-melodic-libpcan
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-sdhlibrary-cpp
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-std-srvs
Requires:       ros-melodic-trajectory-msgs
Requires:       ros-melodic-urdf
BuildRequires:  boost-devel
BuildRequires:  boost-python2-devel
BuildRequires:  boost-python3-devel
BuildRequires:  dpkg
BuildRequires:  libusb-devel
BuildRequires:  ros-melodic-actionlib
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cob-srvs
BuildRequires:  ros-melodic-control-msgs
BuildRequires:  ros-melodic-diagnostic-msgs
BuildRequires:  ros-melodic-libntcan
BuildRequires:  ros-melodic-libpcan
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-roslint
BuildRequires:  ros-melodic-sdhlibrary-cpp
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-std-srvs
BuildRequires:  ros-melodic-trajectory-msgs
BuildRequires:  ros-melodic-urdf

%description
This package provides an interface for operating the schunk dexterous hand
(SDH), including the tactile sensors.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Tue Aug 27 2019 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.13-2
- Autogenerated by Bloom

