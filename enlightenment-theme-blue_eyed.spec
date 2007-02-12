%define	_theme	blue_eyed
Summary:	Blue and minimalistic E17 theme
Summary(pl.UTF-8):   Niebieski i minimalistyczny motyw E17
Name:		enlightenment-theme-%{_theme}
Version:	0.6.5.g_c
Release:	1
License:	BSD
Group:		Themes
Source0:	http://www.get-e.org/Themes/E17/_files/%{_theme}_%{version}.edj
# Source0-md5:	340967a87b751cef3f71f3a367a6db30
URL:		http://www.get-e.org/Themes/E17/
Requires:	enlightenment
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Blue and minimalistic E17 theme.

%description -l pl.UTF-8
Niebieski i minimalistyczny motyw E17.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/enlightenment/data/themes

install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/enlightenment/data/themes/%{_theme}.edj

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/enlightenment/data/themes/%{_theme}.edj
