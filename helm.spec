Name:           helm
Version:        0.9.0
Release:        1%{?dist}
Summary:        A polyphonic synth with lots of modulation

License:       	GPLv3+
URL:           	http://tytel.org/helm
Source0:       	https://github.com/mtytel/helm/archive/v%{version}.tar.gz

BuildRequires:  alsa-lib-devel
BuildRequires:  freetype-devel
BuildRequires:  libcurl-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXinerama-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  libXcursor-devel
Requires:       %{name}-patches = %{version}-%{release}

%global common_desc \
Helm is a polyphonic synthesizer. You use it to create electronic music on\
your computer.

%description
%common_desc

The plugins are available in LV2, VST, AU, AAX and standalone JACK formats.
This package contains the common files and the standalone JACK plugin.

%package -n %{name}-patches
Summary:        Helm plugin in LV2 format
License:        CC-BY
BuildArch:      noarch

%description -n %{name}-patches
%common_desc

This package contains the factory preset patches.

%package -n lv2-%{name}-plugins
Summary:        Helm plugin in LV2 format
Requires:       %{name}-patches = %{version}-%{release}

%description -n lv2-%{name}-plugins
%common_desc

This package contains the LV2 plugin.

%package -n vst-%{name}-plugins
Summary:        Helm plugin in VST format
Requires:       %{name}-patches = %{version}-%{release}

%description -n vst-%{name}-plugins
%common_desc

This package contains the VST plugin.

%prep
%autosetup

%build
%configure
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install LIBDIR=%{_libdir}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_docdir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/%{name}/icons/
%{_mandir}/man1/%{name}*

%files -n %{name}-patches
%license "patches/Factory Presets/LICENSE"
%{_datadir}/%{name}/patches/

%files -n lv2-%{name}-plugins
%{_libdir}/lv2/%{name}.lv2/

%files -n vst-%{name}-plugins
%{_libdir}/lxvst/%{name}.so

%changelog
* Fri Jan 24 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.9.0-1
- Initial build
