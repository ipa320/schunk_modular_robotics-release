Name:           ros-indigo-schunk-libm5api
Version:        0.6.12
Release:        0%{?dist}
Summary:        ROS schunk_libm5api package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://ros.org/wiki/schunk_libm5api
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-libntcan
Requires:       ros-indigo-libpcan
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-libntcan
BuildRequires:  ros-indigo-libpcan

%description
This package wraps the libm5api to use it as a ros dependency. Original sources
from http://www.schunk-modular-
robotics.com/fileadmin/user_upload/software/schunk_libm5api_source.zip.

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Thu Aug 16 2018 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.12-0
- Autogenerated by Bloom

* Sat Jul 21 2018 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.11-0
- Autogenerated by Bloom

* Sun Jan 07 2018 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.10-0
- Autogenerated by Bloom

* Mon Jul 17 2017 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.9-0
- Autogenerated by Bloom

* Mon Oct 10 2016 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.8-0
- Autogenerated by Bloom

* Fri Apr 01 2016 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.7-0
- Autogenerated by Bloom

* Tue Sep 01 2015 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.6-0
- Autogenerated by Bloom

* Mon Aug 31 2015 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.5-0
- Autogenerated by Bloom

* Tue Aug 25 2015 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.4-0
- Autogenerated by Bloom

* Wed Jun 17 2015 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.3-0
- Autogenerated by Bloom

